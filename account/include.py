from .models import *


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