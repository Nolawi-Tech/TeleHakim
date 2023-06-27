from django.urls import path
from payment import views

app_name = "pay"

urlpatterns = [
    path('pay/chapa/', views.KinfeView.as_view(), name='pay_with_chapa')
]
