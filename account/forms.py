from django import forms
from .models import Patient, Doctor

class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Password', "minlength":'4'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth mm/dd/yyyy'}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file', 'placeholder': 'Photo'}),
        }

class DoctorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Password', "minlength":'4'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'specilization': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'specilization'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth mm/dd/yyyy'}),
            'document': forms.FileInput(attrs={'class': 'form-control-file', 'placeholder': 'Documents | tempo | valid certi. attached together in one file'}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file', 'placeholder': 'Photo'}),
        }