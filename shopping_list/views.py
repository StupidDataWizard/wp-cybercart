from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import List, Item, Shop
from django.urls import reverse

# Create your views here.

def index(request):
    context = {}
    context["lists"] = List.objects.all()
    context["shops"] = Shop.objects.all()
    return render(request, "shopping_list/index.html", context)


def add_list(request):
    if "list_name" in request.POST: # Einmal ohne create
        list = List()
        list.name = request.POST["list_name"]
        #print("list_name: ",list.name)
        if list.name != None and list.name != "":
            list.save()
    #List.objects.create(name=request.POST["list_name"])
    return redirect('shopping_list:index')


def add_shop(request): #Einmal mit create
    if "shop_name" in request.POST:
        shop_name = request.POST["shop_name"]
        if shop_name != None and shop_name != "":
            Shop.objects.create(name=request.POST["shop_name"])   
    return redirect('shopping_list:index')


def detail_list(request,list_id):
    context = {}
    context["list"] = get_object_or_404(List, pk=list_id)
    context["items"] = Item.objects.filter(list=list_id)
    context["shops"] = Shop.objects.all() # Wird für die add_item shop selection benötigt
    return render(request, 'shopping_list/detail_list.html', context)


def add_item(request, list_id):   
    list = List.objects.get(pk=list_id)
    if "item_name" in request.POST:   
        item = Item()
        item.name = request.POST["item_name"]
        if item.name != None and item.name != "":
            item.amount = request.POST["item_amount"]
            #item.shop = get_object_or_404(pk=request.POST["shop"])
            item.shop = Shop.objects.get(pk=request.POST["shop"])
            item.list = List.objects.get(pk=list_id)
            item.save()
    return HttpResponseRedirect(reverse('shopping_list:detail_list', args=(list.id,)))
    # Redirect: Generell Empfohlen bei POST/ADD/DELETE/ Sachen ein Redirect zu verwenden!
    # Reverse: Wird verwendet um die URL der genannten Funktion zu bekommen!


def delete_item(request,item_id, list_id):
    item = Item.objects.get(pk=item_id)
    list = List.objects.get(pk=list_id)
    item.delete()
    
    return HttpResponseRedirect(reverse('shopping_list:detail_list', args=(list.id,)))


def detail_shop(request,shop_id):
    context = {}
    context["shop"] = get_object_or_404(Shop, pk=shop_id)
    context["items"] = Item.objects.filter(shop=shop_id)
    #context["shops"] = Shop.objects.all()
    return render(request, 'shopping_list/detail_shop.html', context)


def delete_list(request, list_id):
    list = get_object_or_404(List, pk=list_id)
    list.delete()
    return redirect('shopping_list:index')


def delete_shop(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    shop.delete()
    return redirect('shopping_list:index')


def check_item(request, shop_id, item_id):
    shop = Shop.objects.get(pk=shop_id)
    item = Item.objects.get(pk=item_id)
    item.status = True
    item.save()
    return HttpResponseRedirect(reverse('shopping_list:detail_shop', args=(shop.id,)))
