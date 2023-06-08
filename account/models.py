from django.db import models
import random
import string


class Patient(models.Model):
    first_name = models.CharField(max_length=100, )
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='media/patient_photo', blank=True)

    is_admin = models.BooleanField(max_length=5, default=False)
    is_patient = models.BooleanField(max_length=5, default=False)

    def __str__(self):
        return self.first_name


class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    specilization = models.CharField(max_length=100)
    document = models.FileField(upload_to='media/doctor_document')
    photo = models.ImageField(upload_to='media/doctor_photo', blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name


class Revoke(models.Model):
    ran = ''.join(random.sample(string.ascii_letters + string.digits, k=5))
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    code = models.CharField(max_length=15, blank=True, default=f'TeleHakim:{ran}')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=100, default='pending')

    def __str__(self):
        return self.patient.first_name + ' ' + self.doctor.first_name


class RateDoctor(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    rate = models.IntegerField()

    def __str__(self):
        return self.patient.first_name + ' ' + self.doctor.first_name
