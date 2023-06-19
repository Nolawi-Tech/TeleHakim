from django.shortcuts import redirect, reverse
from django.contrib import messages
from appointment.models import *
from account.include import user_info


def date_spliter(date_list, spliter=60, ):
    night_schedule = []
    day_schedule = []

    for elm in date_list.split(','):
        if elm == "": continue
        tm, t = elm.split(':')
        st, end = tm.split('-')
        for rng in range(int(st), int(end)):
            if t == 'n' or t == 'N':
                if not rng in night_schedule:
                    night_schedule.append(rng)
            else:
                if not rng in day_schedule:
                    day_schedule.append(rng)

    return day_schedule, night_schedule


def add_schedule(due_date, time, doctor):
    sch = "Day"
    for dt in time[0] + ["."] + time[1]:
        if dt == ".":
            sch = "Night"
            continue
        _ls = WorkingDay.objects.filter(doctor=doctor, schedule__exact=f"{dt}:00-{dt + 1}:00 {sch}", date=due_date)

        if not _ls.exists():
            WorkingDay.objects.create(
                doctor=doctor,
                schedule=f"{dt}:00-{dt + 1}:00 {sch}",
                date=due_date
            )


def fill_date(request):
    if request.POST.get('fill_date'):
        first_date = request.POST.get('date-first')
        last_date = request.POST.get('date-final')
        list_date = request.POST.get('date-input')

        try:
            rs = date_spliter(list_date)
        except:
            messages.error(request, "Sorry, Please follow free time input format.")
            return redirect(reverse('dashboard:doctor-dashboard') + '?pages=working_day')
        y, m, d = first_date.split('-')

        email = user_info(request).email
        temp_doc = Doctor.objects.get(email=email)

        if last_date == "":
            add_schedule(f"{y}-{m}-{d}", rs, temp_doc)
        else:
            y2, m2, d2 = last_date.split('-')
            print(d, d2)
            for rdt in range(int(d), int(d2) + 1):
                print(rdt, rs)
                add_schedule(f"{y}-{m}-{rdt}", rs, temp_doc)
    messages.success(request, "Good Job, Your work time added.")
    return redirect(reverse('dashboard:doctor-dashboard') + '?pages=working_day')


def schedule_dtime(request):
    doctor = request.GET.get('doctor')
    sch_id = request.GET.get('sch_id')

    try:
        pt = user_info(request)
        doctor = Doctor.objects.get(email=doctor)
        wk = WorkingDay.objects.get(id=sch_id)
        wk.is_booked = True
        wk.save()
        bk = Appointment(doctor=doctor, patient=pt, schedule=wk)
        bk.save()

        messages.success(request, "Good Job, We have scheduled this specific date for you!")
    except:
        messages.error(request, "Sorry, We cant schedule specific date for you!")

    return redirect(reverse('dashboard:patient-dashboard'))
