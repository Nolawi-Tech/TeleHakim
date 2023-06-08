from django.urls import path
from account.views import *

app_name = 'account'
urlpatterns = [
    path('',login, name="login"),
    path('forgot_password/',forgot_password, name="revoke-new-password"),
    path('update_password_forgot/<str:pk>/', update_password_forgot, name='update_password_forgot'),
    path('logout/', logout, name="logout"),
]