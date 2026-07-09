from decimal import Decimal

from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)

from products.models import Product


def add_to_cart(request, product_id):
    cart = request.session.get("cart", {})
    product = get_object_or_404(
        Product,id=product_id,available=True)
    product_id = str(product.id)
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1
    request.session["cart"] = cart
    return redirect("cart:cart_detail")

def remove_from_cart(request, product_id):
    cart = request.session.get("cart", {})
    product_id = str(product_id)
    if product_id in cart:
        del cart[product_id]
    request.session["cart"] = cart
    return redirect("cart:cart_detail")

def update_cart(request, product_id):
    cart = request.session.get("cart", {})
    quantity = int(request.POST.get("quantity", 1))
    product_id = str(product_id)
    if quantity > 0:
        cart[product_id] = quantity
    else:
        cart.pop(product_id, None)
    request.session["cart"] = cart
    return redirect("cart:cart_detail")

def clear_cart(request):
    request.session["cart"] = {}
    return redirect("cart:cart_detail")

def cart_detail(request):
    cart = request.session.get("cart", {})
    cart_items = []
    total = Decimal("0.00")
    for product_id, quantity in cart.items():
        product = get_object_or_404(
            Product,
            id=product_id
        )
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append(
            {
                "product": product,
                "quantity": quantity,
                "subtotal": subtotal,
            }
        )
    return render(request,"cart/cart.html",{
            "cart_items": cart_items,
            "total": total,})