from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def indexView(request):
    return render(request, 'index.html')

app_name = 'telehakim'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('payment/', include('payment.urls')),
    path('account/', include('account.urls')),
    path('', indexView, name='index'),
]
