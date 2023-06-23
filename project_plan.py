from typing import List

'''

    Admin can interview the doctors,viewing CV, accept or reject, fill some info.
    System's can withhold doctors from working based on 5 user rates.
    Personal profile update, password reset.
    In email using threading.
    
    Admin delete User and some unnecessary actions.
    Timing and Notification sent to user before clock is ticking.
    
    Payment integration.
    Integration b/n prediction and other system -> suggest doctor based on specialization.
    Amaric language support. 
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
