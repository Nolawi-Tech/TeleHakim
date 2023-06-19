from django.db import models
from account.models import Patient, Doctor


class WorkingDay(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, blank=True, null=True)
    schedule = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date) + " " + self.doctor.email + " " + self.schedule


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    schedule = models.ForeignKey(WorkingDay, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.patient.first_name + ' ' + self.doctor.first_name

