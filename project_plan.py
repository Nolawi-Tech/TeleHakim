from typing import List

'''

    
    
    System's can withhold doctors from working based on 5 user rates.
    
    Django administration setup as a superuser.
    Validation for all forms.
    
    In email using threading.
    If one use join it for the other b/c status will be 0.
    Room Id generated for each patient and doctor and store it.
    Admin can interview the doctors,viewing CV, accept or reject, fill some info.
    Doctor view their patients’ medical record
    Patient can see the doctor's rate.
    Personal profile update, password reset.
    Verified Doctor only able to work and apper on search.
    Admin delete User and some unnecessary actions. 
    Timing and Notification sent to user before clock is ticking.
    
    Payment integration.
    Integration b/n prediction and other system -> suggest doctor based on specialization.
    Amahric language support. 
'''


# 0 -> Ongoing
# 1 -> Pending
# 2 -> passed
# 3 -> waiting

class Admin:
    manage_account = True
    view_feedback = True
    patients: List = True
    doctors: List = True
    dashboard: List = doctors

    add_some_info_about = False
    info: List = ['approve', 'update many', 'experience', ]


class Doctor:
    view_rate = True
    schedule: List = True
    dashboard: List = schedule
    working_day = True


class Patient:
    medical_history = True
    write_feedback = True
    book_history = True
    dashboard = book_history
    search = True
    book = True
    rate_doctor = True

    view_his_feedback_and_delete = False


class General:
    register = True
    login = True

    profile = True or False
    reset = True or False

    video_calling = True


def return_date(dt):
    print(dt)


return_date("2AM")
