from django.urls import path
from appointment.views import *

app_name = 'appointment'
urlpatterns = [
    path('fill-date', fill_date, name="fill-date"),
    path('schedule-dtime', schedule_dtime, name="schedule"),
]