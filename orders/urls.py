from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pizza", views.pizza, name="pizza"),
    path("sub", views.sub, name="sub"),
    path("pasta", views.pasta, name="pasta"),
    path("salad", views.salad, name="salad"),
    path("dinnerplatter", views.Dinnerplatter, name="dinnerplatter"),
    path("signup", views.signup, name="signup"),
    path("sign", views.signin, name="signin"),
    path("logout", views.logout, name="logout"),
    path("cart", views.cart, name="cart"),
    path("add_item/<item>/<int:id>", views.add_item, name="add_item"),
    path("place_order", views.place_order, name="place_order"),
    path("remove_item", views.remove_item, name="remove_item"),
    path("order_status", views.order_status, name="order_status"),
]
