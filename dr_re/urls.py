from django.urls import path
from .views import *
urlpatterns = [
    path("",re_home,name="re_home"),
    path("login",login,name="login"),
    path("interview0",interview0,name="interview0"),
    path("interview1",interview1,name="interview1"),
    path("interview2",interview2,name="interview2"),
    path("interview3",interview3,name="interview3"),
    path("interview4",interview4,name="interview4"),
    path("vom_interview",vom_interview,name="vom_interview"),
    
    
    # cough
    path('cough_interview1',cough_interview1,name="cough_interview1"),
    path('cough_interview2',cough_interview2,name="cough_interview2"),
    path('cough_result',cough_result,name='cough_result'),
    
    #headache
    path("headache_interview1",headache_interview1,name='headache_interview1'),
    path("headache_interview2",headache_interview2,name='headache_interview2'),
    path("headache_interview3",headache_interview3,name='headache_interview3'),
    path("headache_result",headache_result,name="headache_result"),
    path("recommend",recommend,name='recommend'),
]