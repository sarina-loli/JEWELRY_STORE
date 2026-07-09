from django.shortcuts import render

# Create your views here.
from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from cart.views import cart_detail
from products.models import Product

from .forms import CheckoutForm
from .models import Order, OrderItem


@login_required
def checkout(request):

    cart = request.session.get("cart", {})

    if not cart:
        return redirect("cart:cart_detail")

    if request.method == "POST":

        form = CheckoutForm(request.POST)

        if form.is_valid():

            order = form.save(commit=False)

            order.customer = request.user

            total = Decimal("0.00")

            order.save()

            for product_id, quantity in cart.items():

                product = Product.objects.get(
                    id=product_id
                )

                subtotal = product.price * quantity

                total += subtotal

                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    price=product.price,
                )

            order.total_price = total

            order.save()

            request.session["cart"] = {}

            return redirect(
                "orders:order_history"
            )

    else:

        form = CheckoutForm()

    return render(
        request,
        "orders/checkout.html",
        {
            "form": form
        }
    )


@login_required
def order_history(request):

    orders = Order.objects.filter(
        customer=request.user
    )

    return render(
        request,
        "orders/order_history.html",
        {
            "orders": orders
        }
    )