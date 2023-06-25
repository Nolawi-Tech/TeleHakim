from django.db import models
from account.models import Patient, Doctor


class Feedback(models.Model):
    class Meta:
        ordering = ('date',)

    user = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=21)
    email = models.EmailField()
    subject = models.CharField(max_length=30, blank=True, null=True)
    body = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.first_name + "'s Comment"


class Rate(models.Model):
    class Meta:
        ordering = ('date',)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, related_name='user_rate')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, related_name='doctor_rate')
    rate = models.IntegerField(default=0)
    comment = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.first_name + " " + self.doctor.first_name


class Prescription(models.Model):
    class Meta:
        ordering = ('date',)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='user_prescription')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_prescription')
    prescription = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.patient.first_name + " " + self.doctor.email


class MedicalHistory(models.Model):
    class Meta:
        ordering = ('date',)
        verbose_name_plural = 'MedicalHistories'
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="patient_mhistory")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="doctor_mdoctor")
    history = models.TextField(max_length=500)
    is_shown = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.patient.first_name + " " + self.doctor.email