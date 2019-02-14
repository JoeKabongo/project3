from django.db import models
from django.contrib.auth.models import User


class Topping(models.Model):
    name = models.CharField(max_length=65)
    def __str__(self):
        return f"{self.name}"

class Pizza(models.Model):
    name = models.CharField(max_length=65)
    small_price = models.FloatField()
    large_price = models.FloatField()

    def __str__(self):
        return f"{self.name}"

class PizzaOrder(models.Model):
    item = models.CharField(max_length=65, default="Pizza")
    name = models.ForeignKey(Pizza, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    price = models.FloatField(default=0)
    completed = models.BooleanField(default=False)
    toppings = models.ManyToManyField(Topping, blank=True, related_name="pizza_topping")


    def __str__(self):
        return f" Small {self.name}" 

class Sub(models.Model):
    name = models.CharField(max_length=65)
    small_price = models.FloatField(null=True, blank=True, default=None)
    large_price = models.FloatField()

    def __str__(self):
        return f"{self.name}"

class SubOrder(models.Model):
    item = models.CharField(max_length=65, default="Sub")
    name = models.ForeignKey(Sub, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    price = models.FloatField(default=0)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} sub"

class DinnerPlatter(models.Model):
    name = models.CharField(max_length=65)
    small_price = models.FloatField()
    large_price = models.FloatField()

    def __str__(self):
        return f"{self.name}"

class DinnerPlatterOrder(models.Model):
    item = models.CharField(max_length=65, default="Dinner Platter")
    name = models.ForeignKey(DinnerPlatter, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    price = models.FloatField(default=0)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

# Create your models here.
class Pasta(models.Model):
    name = models.CharField(max_length=65)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name}"

class PastaOrder(models.Model):
    item = models.CharField(max_length=65, default="Pasta")
    name = models.ForeignKey(Pasta, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    price = models.FloatField(default=0)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

class Salad(models.Model):
    item = models.CharField(max_length=65, default="Salad")
    name = models.CharField(max_length=65)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} "

class SaladOrder(models.Model):
    item = models.CharField(max_length=65, default="Salad")
    name = models.ForeignKey(Salad, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    price = models.FloatField(default=0)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

class PlacedOrder(models.Model):
    dinnerplatter = models.ManyToManyField(DinnerPlatterOrder,blank=True, related_name="dinnerplatter")
    pasta = models.ManyToManyField(PastaOrder,blank=True, related_name="pasta")
    pizza = models.ManyToManyField(PizzaOrder,blank=True, related_name="pizza")
    salad = models.ManyToManyField(SaladOrder,blank=True, related_name="salad")
    sub = models.ManyToManyField(SubOrder,blank=True, related_name="subs")
    total_price = models.FloatField()
    date = models.TimeField()
    user = models.ForeignKey(User,null=True, on_delete=models.PROTECT)
