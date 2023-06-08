from django.shortcuts import render
from account.include import user_info, user_role as u_role
# Create your views here.


def admin_dashboard(request):
    page = request.GET.get('pages')
    user = user_info(request)
    user_role = u_role(request)

    context = {
        'page': page,
        'user': user,
        'user_role': user_role
    }
    return render(request, 'telehakim/admin-page.html', context)


def patient_dashboard(request):
    page = request.GET.get('pages')
    user = user_info(request)
    user_role = u_role(request)

    context = {
        'page': page,
        'user': user,
        'user_role': user_role
    }
    return render(request, 'telehakim/patient-page.html', context)


def doctor_dashboard(request):
    page = request.GET.get('pages')
    user = user_info(request)
    user_role = u_role(request)

    context = {
        'page': page,
        'user': user,
        'user_role': user_role
    }
    return render(request, 'telehakim/doctor-page.html', context)