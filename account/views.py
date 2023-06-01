from django.shortcuts import render
from account.models import *
from account.forms import *
# Create your views here.

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'account/logout.html')

def register(request):
    # register throug post request
    print({name:val for name, val in request.POST.items()})
    if request.method == 'POST':
        acc = Patient.objects.create({name:val for name, val in request.POST.items()})
        acc.save()
        print('register success', acc)

    context = {
        'form': PatientRegistrationForm()
    }
    return render(request, 'register.html' , context)
