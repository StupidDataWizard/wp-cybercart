from django.urls import path
from . import views

app_name = 'shopping_list'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_list', views.add_list, name='add_list'),
    path('add_shop', views.add_shop, name='add_shop'),
    path('detail_list/<int:list_id>', views.detail_list, name='detail_list'),
    path('add_item/<int:list_id>', views.add_item, name='add_item'),
    path('delete_item/<int:item_id>/<int:list_id>', views.delete_item, name='delete_item'),
    path('detail_shop/<int:shop_id>', views.detail_shop, name='detail_shop'),
    path('delete_list/<int:list_id>', views.delete_list, name='delete_list'),
    path('delete_shop/<int:shop_id>', views.delete_shop, name='delete_shop'),
    path('check_item/<int:shop_id>/<int:item_id>', views.check_item, name='check_item')
]

