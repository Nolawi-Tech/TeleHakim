from django.contrib import admin
from account.models import *
# Register your models here.

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Revoke)