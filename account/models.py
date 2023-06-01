from django.db import models

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=100,)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='patient_photo', blank=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    firsT_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    specilization = models.CharField(max_length=100)

    document = models.FileField(upload_to='doctor_document', blank=True)
    photo = models.ImageField(upload_to='patient_photo', blank=True)

    def __str__(self):
        return self.name