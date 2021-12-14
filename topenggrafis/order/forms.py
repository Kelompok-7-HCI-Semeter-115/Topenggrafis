from django import forms
from django.forms import ModelForm
from .models import Customer
from django import forms

class orderForm(ModelForm):
    class Meta:
        model = Customer
        fields = [
            'full_name',
            'email',
            'phone_number',
            'services',
        ]

        widgets = {
            'full_name':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number':forms.TextInput(attrs={'class': 'form-control'}),
            'services':forms.Select(attrs={'class': 'form-control'}),
        }

class searchForm(ModelForm):
    class Meta:
        model = Customer
        fields = [
            'full_name',
        ]

        widgets = {
            'full_name':forms.TextInput(attrs={'placeholder': 'Search by fullname',
                                                'class' : 'form-control'}),
        }