from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import PatientModel, MedicineSellModel, SetUpModel
import os


class PatientForm(forms.ModelForm):
    class Meta:
        model = PatientModel
        fields = "__all__"
        CHOICES = (('Active', 'Active'), ('Inactive', 'Inactive'))
        widgets = {
            'patient_name': forms.TextInput(attrs={'class': 'form-control'}),
            'patient_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'patient_alternative_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'patient_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'patient_status': forms.Select(choices=CHOICES, attrs={'class': 'form-control'}),
            'patient_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class MedicineSellForm(forms.ModelForm):
    class Meta:
        model = MedicineSellModel
        fields = "__all__"
        widgets = {
            "coustomer_name": forms.Select(attrs={'class': 'form-control select_box'}),
            "coustomer_contact": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coustomer Contact'}),
            "medicine_buy_date": forms.DateInput(format='%m/%d/%Y',
                                                 attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                        'type': 'date'}),

        }


class SetupForm(forms.ModelForm):
    class Meta:
        model = SetUpModel
        fields = "__all__"
        widgets = {
            'company_title': forms.TextInput(attrs={'class': 'form-control'}),
            'company_address': forms.Textarea(attrs={'class': 'form-control'}),
            'company_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'company_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'company_logo': forms.FileInput(attrs={'id': 'inputFile'})
        }


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


