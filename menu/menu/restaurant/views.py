from django.shortcuts import render, redirect
from .models import FoodItem, Order, OrderItem

def home(request):
    return render(request, 'restaurant/home.html')

def menu(request):
    context = {
        'food_items':FoodItem.objects.all()
    }
    
    return render(request, 'restaurant/menu.html', context)

def cart(request):
    cart = request.session.get('cart', {})
    total_price = 0
    items = []
    for item_id, quantity in cart.items():
        food_item = FoodItem.objects.get(id=item_id)
        total_price += food_item.price * quantity
        items.append({'food_item': food_item, 'quantity': quantity})
    return render(request, 'restaurant/cart.html', {'items': items, 'total_price': total_price})
    

def add_to_cart(request, item_id):
    if 'cart' not in request.session:
        request.session['cart']= {}

    cart = request.session['cart']
    cart[item_id] = cart.get(item_id, 0) + 1
    request.session.modified = True  
    return redirect('menu')