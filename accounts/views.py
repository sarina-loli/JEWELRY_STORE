from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from products import views
from .forms import RegisterForm, ProfileForm
from .models import Profile
from django.contrib.auth import logout



def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            Profile.objects.create(
                user=user
            )

            login(request, user)

            return redirect("products:product_list")

    else:
        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )


@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
   
    

    if request.method == "POST":

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()

            return redirect("accounts:profile")

    else:

        form = ProfileForm(
            instance=profile
        )

    return render(
        request,
        "accounts/profile.html",
        {
            "form": form
        }
    )
from orders.models import Order


@login_required
def dashboard(request):

    orders = Order.objects.filter(
        customer=request.user
    ).order_by("-order_date")

    return render(
        request,
        "accounts/dashboard.html",
        {
            "orders": orders
        }
    )
@login_required
def logout_view(request):
    logout(request)
    return redirect('products:product_list')
