from django.db import models
from uuid import uuid4
from account.models import Patient


class yenepayStatus(models.TextChoices):
 
    PENDING = 'pending', 'PENDING'
    SUCCESS = 'success', 'SUCCESS'
    CREATED = 'created', 'CREATED'
    FAILED = 'failed', 'FAILED'


class yenepayTransactionMixin(models.Model):
    class Meta:
        ordering = ('date',)

    id = models.UUIDField(primary_key=True, default=uuid4)

    amount = models.FloatField()
    currency = models.CharField(max_length=25, default='ETB')
    email = models.EmailField()
    user = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    description = models.TextField()

    event = models.CharField(max_length=255, null=True, blank=True)

    status = models.CharField(max_length=50, choices=yenepayStatus.choices, default=yenepayStatus.CREATED)

    response_dump = models.JSONField(default=dict)  # incase the response is valuable in the future

    class Meta:
        abstract = False

    def __str__(self) -> str:
        return f"{self.user} | {self.amount}"
    
    def serialize(self) -> dict:
        return {
            'amount': self.amount,
            'currency': self.currency,
            'email': self.email,
            'user': self.user,
            'description': self.description
        }

# TODO: add non abstract model


class yenepayTransaction(yenepayTransactionMixin):
    pass
