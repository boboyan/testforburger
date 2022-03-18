from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
# importing loading from django template
from django.template import loader
from django.db.models import Sum
from _decimal import Decimal

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate  # add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm  # add this
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import *
from .forms import *
from django.contrib import messages  # import messages
from .forms import SignUpForm


# our view which is a function named index
def index(request):
    # getting our template
    template = loader.get_template('aboutus/homepage.html')
    # rendering the template in HttpResponse
    return HttpResponse(template.render())


def products(request):
    return render(request, 'aboutus/products.html', {'products': products})


def shop(request):
    return render(request, 'aboutus/shop.html', {'shop': shop})


def aboutus(request):
    return render(request, 'aboutus/aboutus.html', {'aboutus': aboutus})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'aboutus/signup.html', {'form': form})


# now = timezone.now()

def contactus(request):
    return render(request, 'aboutus/contactus.html', {'contactus': contactus})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("burgerwebsite:homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="burgerwebsite/login.html", context={"login_form": form})
