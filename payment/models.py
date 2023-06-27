from django.db import models
from uuid import uuid4
from account.models import Patient, Doctor


class ChapaStatus(models.TextChoices):
    PENDING = 'pending', 'PENDING'
    SUCCESS = 'success', 'SUCCESS'
    CREATED = 'created', 'CREATED'
    FAILED = 'failed', 'FAILED'


class Transaction(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    amount = models.FloatField()
    appointment_id = models.BigIntegerField(blank=True, null=True)
    is_used = models.BooleanField(default=False)

    class Meta:
        abstract = False

    def __str__(self) -> str:
        return f"{self.patient.first_name} | {self.amount}"

    def serialize(self) -> dict:
        return {
            'amount': self.amount,
            'email': self.patient.email,
        }


class ChapaTransaction(Transaction):
    pass
