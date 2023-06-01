from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('payment.urls')),
    path('recommend/', include('dr_re.urls'), name="recommend"),
]
