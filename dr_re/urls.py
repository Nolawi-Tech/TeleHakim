from django.urls import path
from .views import *
urlpatterns = [
    path("",re_home,name="re_home"),
    path("interview0",interview0,name="interview0"),
    path("interview1",interview1,name="interview1"),
    path("interview2",interview2,name="interview2"),
    path("interview3",interview3,name="interview3"),
    path("interview4",interview4,name="interview4"),
    path("vom_interview",vom_interview,name="vom_interview"),
    path('cough_interview1',cough_interview1,name="cough_interview1"),
    path("recommend",recommend,name='recommend'),
]