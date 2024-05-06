from django.db import models

class List(models.Model):
    name = models.CharField(max_length=200)

    def checked(self):
        return Item.objects.filter(list=self, status=True).count()

    def total(self):
        return Item.objects.filter(list=self).count()

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    shop = models.ForeignKey(to="Shop", on_delete=models.SET_NULL, null=True)
    list = models.ForeignKey(to="List", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=100)
    prevalence = models.IntegerField(default=0)

    def __str__(self):
        return self.name


