from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import orderForm
from .models import Customer

# Create your views here.
def home(request):
    return render(request, 'index.html')

def order(request):
    if request.method == "POST":
        form = orderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = orderForm()

    return render(request, 'order.html', {'form': form})