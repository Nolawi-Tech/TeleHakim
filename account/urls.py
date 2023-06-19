from django.urls import path
from account.views import *

app_name = 'account'
urlpatterns = [
    path('', login, name="login"),
    path('forgot_password/', forgot_password, name="revoke-new-password"),
    path('register_patient/<str:_to>/', register_patient, name="register-patient"),
    path('register_doctor/<str:_from>/', register_doctor, name="register-doctor"),
    path('delete/<str:pk>/<str:role>/', delete_user, name="delete-user"),
    path('update_password_forgot/<str:pk>/', update_password_forgot, name='update_password_forgot'),
    path('logout/', logout, name="logout"),
]