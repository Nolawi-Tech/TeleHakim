from django.shortcuts import render, redirect
from account.models import *
from account.forms import *
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            patient = Patient.objects.get(email=email)
            if patient.password == password:

                request.session['role'] = 'patient'
                request.session['email'] = patient.email

                messages.success(request, "You are successfully logged in.")
                return redirect('/')
            else:
                messages.error(request, "Invalid Password, Please try again.")
        except:
            messages.error(request, "Invalid Email, Please try again.")
    return render(request, 'login.html')

def logout(request):

    return render(request, 'account/logout.html')

def register(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Welcome, you are successfully registered.")
            return redirect('account:login')
        else:
            messages.error(request, "Not Valid Form, please fill form accordingly or may account exist.")
    context = {
        'form': PatientRegistrationForm()
    }
    return render(request, 'register.html' , context)
