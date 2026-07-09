from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def product_list(request):

    products = Product.objects.filter(
        available=True
    )

    categories = Category.objects.all()

    return render(
        request,
        "products/product_list.html",
        {
            "products": products,
            "categories": categories,
        },
    )


def product_detail(request, slug):

    product = get_object_or_404(
        Product,
        slug=slug,
        available=True,
    )

    return render(
        request,
        "products/product_detail.html",
        {
            "product": product,
        },
    )