from .models import *
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from appointment.models import Appointment


def user_role(request):
    status = request.session.get('user-role', None)
    return status


def user_info(request):
    email = request.session.get("email", None)
    us = None
    if email is not None:
        try:
            ls_us = Patient.objects.filter(email=email)
            ls_dr = Doctor.objects.filter(email=email)
            if len(ls_us) > 0:
                us = ls_us[0]
            elif len(ls_dr) > 0:
                us = ls_dr[0]
        except:
            pass
    return us


def send_email(link, to, content):
    try:
        html_content = render_to_string(link, content)
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            'TeleHakim System',
            text_content,
            'mesaye2010@gmail.com',
            to,
        )
        email.attach_alternative(html_content, "text/html")
        return email.send() > 0
    except:
        return False


def automate_email(request):
    app = Appointment.objects.filter()
    for ap in app:
        if not ap.is_notified:
            if (ap.left_time.total_seconds() > 0) and (ap.left_time.total_seconds() < 1800):
                a = send_email('email/appointment_reminder.html', [ap.patient.email], {'name': ap.patient.first_name})
                b = send_email('email/appointment_reminder.html', [ap.doctor.email], {'name': ap.doctor.first_name})
                if a or b:
                    ap.is_notified = True
                    ap.save()
