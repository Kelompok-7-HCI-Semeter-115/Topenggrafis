from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import orderForm, searchForm
from .models import Customer

# Create your views here.
def home(request):
    return render(request, 'index.html')

def list(request):
    cust = Customer.objects.all()
    form = searchForm(request.POST or None)
    context = {
            "form": form,
            "cust": cust,
        }
    if request.method == "POST": 
        cust = Customer.objects.filter(full_name__icontains=form['full_name'].value(),
                                            )
        context = {
            "form": form,
            "cust": cust,
        }

    return render(request, 'list.html',context)

def order(request):
    if request.method == "POST":
        form = orderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = orderForm()

    return render(request, 'order.html', {'form': form})