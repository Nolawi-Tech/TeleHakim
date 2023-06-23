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
    photo = models.ImageField(upload_to='patient_photo', blank=True, default='user_avatar.png')

    is_admin = models.BooleanField(max_length=5, default=False)
    is_patient = models.BooleanField(max_length=5, default=False)

    def __str__(self):
        return self.first_name


class Doctor(models.Model):
    SPECIALITY_CHOICES = [
        ('Dermatologist', 'Dermatologist'),
        ('Dentist', 'Dentist'),
        ('Sexologist', 'Sexologist'),
        ('Dietitian/Nutritionist', 'Dietitian/Nutritionist'),
        ('General Physician', 'General Physician'),
        ('Orthopedist', 'Orthopedist'),
        ('Gynaecologist', 'Gynaecologist'),
        ('Pediatrics', 'Pediatrics'),
        ('Psychologist', 'Psychologist'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    specialization = models.CharField(max_length=100, choices=SPECIALITY_CHOICES)
    document = models.FileField(upload_to='doctor_document')
    photo = models.ImageField(upload_to='doctor_photo', blank=True, default='user_avatar.png')
    is_verified = models.BooleanField(default=False)

    degree = models.CharField(max_length=100, null=True, blank=True)
    experience = models.CharField(max_length=100, default='0')
    about = models.TextField(max_length=500, null=True, blank=True)
    fee = models.IntegerField(default=0)
    hospital = models.CharField(max_length=100, null=True, blank=True)
    account_number = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.first_name


class Revoke(models.Model):
    ran = ''.join(random.sample(string.digits, k=6))
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True, null=True)
    code = models.CharField(max_length=15, blank=True, default=ran)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code


