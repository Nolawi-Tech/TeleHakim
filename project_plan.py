from typing import List

# passed date must be filtered and not show to user.
# Some medical History may or may not be seen by User.
# doctor must be able to remove his working day.

# 0 -> Ongoing
# 1 -> Pending
# 2 -> passed


class Admin:
    manage_account = True
    view_feedback = True
    patients: List = True
    doctors: List = True
    dashboard: List = doctors

    add_some_info_about = False
    info:List = ['approve', 'update many', 'experience', ]


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

    view_his_feedback_a_delete = False


class General:
    register = True
    login = True

    profile = True or False
    reset = True or False

    video_calling = False

