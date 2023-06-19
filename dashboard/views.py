from django.shortcuts import render, redirect
from account.models import *
from dashboard.models import *
from appointment.models import *
from django.contrib import messages
from account.include import user_info, user_role as u_role
from account.forms import PatientRegistrationForm, DoctorRegistrationForm


# Create your views here.


def admin_dashboard(request):
    page = request.GET.get('pages')
    user = user_info(request)
    user_role = u_role(request)

    context = {
        'page': page,
        'user': user,
        'user_role': user_role,

        'patients': Patient.objects.all(),
        'doctors': Doctor.objects.all(),
        'admins': Patient.objects.filter(is_admin=True),
        'feedbacks': Feedback.objects.all(),
        'patient_form': PatientRegistrationForm(),
        'doctor_form': DoctorRegistrationForm(),
    }
    return render(request, 'telehakim/admin-page.html', context)


def patient_dashboard(request):
    page = request.GET.get('pages')
    user = user_info(request)
    user_role = u_role(request)

    unique_dates = []
    list_schedule = []
    doctors = Doctor.objects.all()

    if request.method == "POST":
        if request.POST.get('feedback') is not None:
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            fd = Feedback(user=user, name=name, email=email, subject=subject, body=message)
            try:
                fd.save()
                messages.success(request, "Thank you, we value your feedback.")
            except:
                messages.error(request, "Sorry, we can't add your feedback.")
        if request.POST.get('search') is not None:
            min_price = request.POST.get('min_price')
            max_price = request.POST.get('max_price')
            specialization = request.POST.getlist('specialization')[0]

            if min_price:
                doctors = doctors.filter(fee__gt=min_price)
            if max_price:
                doctors = doctors.filter(fee__lt=max_price)
            if specialization:
                doctors = doctors.filter(specialization=specialization)
        if request.POST.get('rate_doctor') is not None:
            id = request.POST.get('email')
            comment = request.POST.get('comment')
            rate = request.POST.get('range')
            try:
                doc = Doctor.objects.get(id=id)
                rt = Rate(doctor=doc, user=user, rate=int(rate), comment=comment)
                rt.save()
                messages.success(request, "Thank you, for rating doctors.")
                return redirect('dashboard:patient-dashboard')
            except:
                messages.error(request, "Sorry, we can't add your rating.")
    if request.GET.get('list_date'):
        email = request.GET.get('doc_email')
        date = request.GET.get('date')
        try:
            doctor = Doctor.objects.get(email=email)
            list_schedule = WorkingDay.objects.filter(doctor=doctor).filter(is_booked=False)
            if date != "":
                list_schedule = list_schedule.filter(date=date)

            for sch in list_schedule:
                if not sch.date in unique_dates:
                    unique_dates.append(sch.date)
        except:
            messages.error(request, "Sorry, we can't find any doctor or provide email.")

    context = {
        'page': page,
        'user': user,
        'user_role': user_role,
        'doctors': doctors,
        'histories': Appointment.objects.filter(patient=user).order_by('status'),
        'prescriptions': Prescription.objects.filter(patient=user),
        'medical_histories': MedicalHistory.objects.filter(patient=user, is_shown=True),
        'book_info': {
            'dates': sorted(unique_dates)[:6],
            'schedules': list_schedule,
            'doc_email': request.GET.get('doc_email'),
        },
        'patient_form': PatientRegistrationForm(),
    }
    return render(request, 'telehakim/patient-page.html', context)


def doctor_dashboard(request):
    page = request.GET.get('pages')
    user = user_info(request)
    user_role = u_role(request)
    rates = Rate.objects.all()

    if request.method == "POST":
        if request.POST.get('set_md_history') is not None:
            # set to MedicalHistory model find patient with id, and doctor is current user
            id = request.POST.get('id')
            is_shown = request.POST.get('is_shown')
            md_history = request.POST.get('md_history')
            if is_shown == "on":
                is_shown = False
            else:
                is_shown = True
            try:
                patient = Patient.objects.get(id=id)
                md = MedicalHistory(patient=patient, doctor=user, is_shown=is_shown, history=md_history)
                md.save()
                messages.success(request, "Thank you, for adding medical history.")
                return redirect('dashboard:doctor-dashboard')
            except:
                messages.error(request, "Sorry, we can't add your medical history.")
        if request.POST.get('set_prescription') is not None:
            id = request.POST.get('id')
            prescription = request.POST.get('prescription')
            try:
                patient = Patient.objects.get(id=id)
                pr = Prescription(patient=patient, doctor=user, prescription=prescription)
                pr.save()
                messages.success(request, "Thank you, for adding prescription.")
                return redirect('dashboard:doctor-dashboard')
            except:
                messages.error(request, "Sorry, we can't add your prescription.")
    context = {
        'page': page,
        'user': user,
        'user_role': user_role,
        'histories': Appointment.objects.filter(doctor=user).order_by('status'),
        'rate_info': {
            'rates': rates,
            'total_percent': ((sum(obj.rate for obj in rates)+0.01) / ((10 * len(rates))+0.01)) * 100,
        },
        'doctor_form': DoctorRegistrationForm(),
    }
    return render(request, 'telehakim/doctor-page.html', context)
