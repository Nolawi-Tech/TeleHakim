import requests
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from .models import *
from chapa import Chapa
from account.models import *
from django.views.generic import View
from django.utils.crypto import get_random_string
from django.http import HttpResponseRedirect
from django.http import QueryDict
from urllib.parse import *
from .models import Transaction
from django.contrib import messages


class KinfeView(View):

    def get(self, request, *args, **kwargs):
        doc_email = request.GET.get('doctor')
        pt_email = request.GET.get('patient')

        doc = Doctor.objects.get(email=doc_email)
        pt = Patient.objects.get(email=pt_email)

        try:
            SECRET = settings.CHAPA_SECRET
            API_URL = settings.CHAPA_API_URL
            API_VERSION = settings.CHAPA_API_VERSION
            CALLBACK_URL = settings.CHAPA_WEBHOOK_URL
            TRANSACTION_MODEL = settings.CHAPA_TRANSACTION_MODEL
        except AttributeError:
            raise ImproperlyConfigured("One or more chapa config missing, please check in your settings file")

        data = {
            'amount': doc.fee,
            'currency': 'ETB',
            'email': pt.email,
            'first_name': pt.first_name,
            'last_name': pt.last_name,
            'tx_ref': get_random_string(10),
            "return_url": "http://127.0.0.1:8000/dashboard/patient/?pages=payment",
            'callback_url': 'https://webhook.site/077164d6-29cb-40df-ba29-8a00e59a7e60',
            'description': 'Tele-Hakim payment'
        }

        Transaction.objects.create(
            patient=pt,
            doctor=doc,
            amount=doc.fee,
        )

        chapa = Chapa(SECRET)
        response = chapa.initialize(**data)
        if response.get('data', False):
            url = response.get('data').get('checkout_url')
            return HttpResponseRedirect(url)
        print(response)
        messages.success(request, "Payment Successful, Book an appointment with the doctor")
        return HttpResponseRedirect('/dashboard/patient/?pages=search')

