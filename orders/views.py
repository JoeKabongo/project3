from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from .models import Pasta, DinnerPlatter, Pizza, Salad, Sub, Topping, PizzaOrder, SaladOrder, DinnerPlatterOrder, SubOrder, PastaOrder, PlacedOrder
from django.db.models import Sum
from django.core.mail import send_mail
import json
import datetime


# Create your views here.
def index(request):
    return render(request, "orders/index.html")

def pizza(request):
    context = {
        "item": "Pizza",
        "menu": Pizza.objects.all(),
        "size":True,
        "addtional_steps":True,
        "toppings":Topping.objects.all(),
    }
    return render(request, "orders/item.html", context)

def sub(request):
    context = {
        "item": "Sub",
        "menu": Sub.objects.all(),
        "size":True,
        "addtional_steps":True,
    }
    return render(request, "orders/item.html", context)

def pasta(request):
    context = {
        "item" : "Pasta",
        "menu": Pasta.objects.all(),
    }
    return render(request, "orders/item.html", context)

def salad(request):
    context = {
        "item":"Salad",
        "menu": Salad.objects.all(),
    }
    return render(request, "orders/item.html", context)

def Dinnerplatter(request):
    context = {
        "item":"Dinner Platter",
        "menu": DinnerPlatter.objects.all(),
        "size":True,
    }
    return render(request, "orders/item.html", context)

def signup(request):
    """
        Sign up function that allow the user to signup
    """
    if request.method == 'GET':
        return render(request, "orders/signup.html")
    else:
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm-password"]

        #check that password matches
        if password != confirm_password:
            raise Http404("Password does not match")

        #make sure the email is unique
        try:
            u = User.objects.get(email=email)
            raise Http404("email has already been taken sorry")

        except:
            #handle error if the username has already been taken
            try:
                user = User.objects.create_user(username, email, password)
            except:
                raise Http404("Username has already been taken sorry")

            auth.login(request, user)
            return HttpResponseRedirect(reverse("index"))

def signin(request):
    if request.method == 'GET':
        return render(request, "orders/signin.html")
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        #check if the user exist
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            context = {
                "error":True,
            }
            return render(request, "orders/signin.html", context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("index"))

def cart(request):
    """
        Allow user to see what they have inside their shopping cart
    """
    if request.user.is_anonymous:
        return HttpResponseRedirect(reverse("index"))
    user = request.user

    orders = [PizzaOrder.objects.filter(user=user, completed=False),SaladOrder.objects.filter(user=user, completed=False),
              SubOrder.objects.filter(user=user, completed=False), DinnerPlatterOrder.objects.filter(user=user, completed=False),
              PastaOrder.objects.filter(user=user, completed=False)]
    total_price = 0
    for order in orders:
        if len(order) != 0:
            total_price += order.aggregate(Sum('price'))['price__sum']

    to_display = []
    for order in orders:
        for item in order:
            m = {}
            m["item"] = item.item
            m["id"] = item.id
            m["name"] = item.name
            m["price"] = item.price
            try:
                m["toppings"] = item.toppings.all()
            except  AttributeError:
                pass
            to_display.append(m)

    total_price = round(total_price, 2)
    print(total_price)

    context = {
        "orders":to_display,
        "total_price":total_price,
    }
    if total_price == 0:
        context["no_item"] = True


    return render(request, "orders/cart.html", context)

def add_item(request, item, id):
    """
        add item to cart
    """
    price = request.POST["price"]
    print(f" price{price}")
    print(f"item {item}")
    print(f"id {id}")
    user = request.user
    name=""
    if item== "Pizza":
        pizza = Pizza.objects.get(pk=id)
        name = pizza.name

        toppings = json.loads(request.POST["toppings"])
        order = PizzaOrder(name=pizza, price=price,user=user)
        order.save()

        for topping in toppings:
            t = Topping.objects.get(pk=topping)
            order.toppings.add(t)
        order.save()

    elif item =="Sub":
        sub = Sub.objects.get(pk=id)
        name = sub.name
        order = SubOrder(name=sub, price=price,user=user)
        order.save()
    elif item =="Pasta":
        pasta = Pasta.objects.get(pk=id)
        name = pasta.name
        order = PastaOrder(name=pasta, price=price,user=user)
        order.save()
    elif item =="Salad":
        salad = Salad.objects.get(pk=id)
        name=salad.name
        order = SaladOrder(name=salad, price=price,user=user)
        order.save()
    elif item =="Dinner":
        dinner = DinnerPlatter.objects.get(pk=id)
        name = dinner.name
        order = DinnerPlatterOrder(name=dinner, price=price, user=user)
        order.save()
    else:
        data = {
            "error":True
        }

        return JsonResponse(data)

    data = {
        "name":name,
        "error":False
    }
    return JsonResponse(data)

def remove_item(request):
    """
        Remove an item from the shopping cart
    """
    data = {

    }
    id = request.POST['id']
    table = request.POST['table']

    if table == "Pizza":
        PizzaOrder.objects.get(pk=id).delete()
    elif table == "Sub":
        SubOrder.objects.get(pk=id).delete()
    elif table == "Salad":
        SaladOrder.objects.get(pk=id).delete()
    elif table == "Pasta":
        PastaOrder.objects.get(pk=id).delete()
    elif table == "Dinner Platter":
        DinnerPlatterOrder.objects.get(pk=id).delete()
    else:
        return Http404("Something went wrong")
    return JsonResponse(data)


def place_order(request):
    """

    """
    total = request.POST["total_price"]

    data = {
        'total':total
    }
    user = request.user
    orders = {"Pizza":PizzaOrder.objects.filter(user=user, completed=False), "Salad":SaladOrder.objects.filter(user=user, completed=False),
              "Sub":SubOrder.objects.filter(user=user, completed=False), "Dinner":DinnerPlatterOrder.objects.filter(user=user, completed=False),
              "Pasta":PastaOrder.objects.filter(user=user, completed=False)}
    completed_order = PlacedOrder(total_price=total, date = datetime.datetime.now(), user = request.user)
    completed_order.save()

    #add order to completed order models so that admin can see past order
    if orders["Pizza"] is not None:
        pizzas = orders["Pizza"]
        for order in pizzas:
            order.completed = True
            order.save()
            completed_order.pizza.add(order)
            completed_order.save()

    if orders["Salad"] is not None:
        salads = orders["Salad"]
        for order in salads:
            order.completed = True
            order.save()
            completed_order.salad.add(order)
            completed_order.save()


    if orders["Sub"] is not None:
        subs = orders["Sub"]
        for order in subs:
            order.completed = True
            order.save()
            completed_order.sub.add(order)
            completed_order.save()

    if orders["Dinner"] is not None:
        dinner_platter = orders["Dinner"]
        for order in dinner_platter:
            order.completed = True
            order.save()
            completed_order.dinnerplatter.add(order)
            completed_order.save()


    if orders["Pasta"] is not None:
        pasta = orders["Pasta"]
        for order in pasta:
            order.completed = True
            order.save()
            completed_order.pasta.add(order)
            completed_order.save()
    return JsonResponse(data)

def order_status(request):
    """
    """

    return Http404("my name is jonathan")
