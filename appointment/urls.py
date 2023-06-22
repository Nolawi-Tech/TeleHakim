from django.urls import path
from appointment.views import *

app_name = 'appointment'
urlpatterns = [
    path('fill-date', fill_date, name="fill-date"),
    path('schedule-dtime', schedule_dtime, name="schedule"),
    path('test', test, name="test"),
    path('change_status/<str:id>/<str:option>', change_status, name="change_status"),
]