from django.contrib import admin
from .models import Pasta, DinnerPlatter, Pizza, Salad, Sub, Topping, PizzaOrder, SaladOrder, DinnerPlatterOrder, SubOrder, PastaOrder, PlacedOrder

# Register your models here.
admin.site.register(Pasta)
admin.site.register(DinnerPlatter)
admin.site.register(Pizza)
admin.site.register(Sub)
admin.site.register(Topping)
admin.site.register(PizzaOrder)
admin.site.register(SaladOrder)
admin.site.register(DinnerPlatterOrder)
admin.site.register(SubOrder)
admin.site.register(PastaOrder)
admin.site.register(PlacedOrder)
