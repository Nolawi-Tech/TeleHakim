from django import forms
from .models import Patient

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
