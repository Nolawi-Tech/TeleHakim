from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from account.models import Doctor
import pandas as pd
import joblib
import os
# from django.conf.settings import PROJECT_ROOT

from django.conf import settings


# Create your views here
# 

def mian(request):
    return render(request, 'recommendation/mian.html')


symptom = ['high_fever', 'nausea', 'skin_rash', 'yellowish_skin', 'itching', 'mild_fever', 'vomiting', 'fatigue',
           'abnormal_menstruation', 'muscle_weakness', 'indigestion', 'joint_pain', 'yellowing_of_eyes', 'headache',
           'blurred_and_distorted_vision', 'continuous_feel_of_urine', 'prominent_veins_on_calf', 'sweating',
           'altered_sensorium', 'lack_of_concentration', 'neck_pain', 'abdominal_pain', 'irritation_in_anus', 'chills',
           'shivering', 'sunken_eyes', 'breathlessness', 'hip_joint_pain', 'cough', 'ulcers_on_tongue', 'dark_urine',
           'loss_of_appetite', 'weight_loss', 'irregular_sugar_level', 'malaise', 'rusty_sputum', 'chest_pain',
           'mucoid_sputum', 'diarrhoea', 'family_history', 'phlegm', 'muscle_pain', 'congestion', 'patches_in_throat',
           'loss_of_balance', 'unsteadiness', 'stomach_pain', 'spotting_ urination', 'dizziness', 'dischromic _patches',
           'inflammatory_nails', 'acidity', 'stiff_neck', 'extra_marital_contacts', 'red_sore_around_nose', 'anxiety',
           'scurring', 'burning_micturition', 'toxic_look_(typhos)', 'dehydration', 'blackheads',
           'pain_during_bowel_movements', 'nodal_skin_eruptions', 'belly_pain', 'knee_pain', 'back_pain', 'coma',
           'excessive_hunger', 'pus_filled_pimples', 'muscle_wasting', 'blister', 'pain_behind_the_eyes',
           'receiving_unsterile_injections', 'continuous_sneezing', 'silver_like_dusting', 'depression',
           'spinning_movements', 'swollen_extremeties', 'yellow_crust_ooze', 'weakness_in_limbs', 'passage_of_gases',
           'polyuria', 'painful_walking', 'red_spots_over_body', 'constipation', 'bladder_discomfort', 'slurred_speech',
           'small_dents_in_nails', 'obesity', 'distention_of_abdomen', 'watering_from_eyes',
           'weakness_of_one_body_side', 'internal_itching', 'throat_irritation', 'swelling_joints', 'fluid_overload.1',
           'acute_liver_failure', 'visual_disturbances', 'bruising', 'foul_smell_of urine', 'movement_stiffness',
           'weight_gain', 'stomach_bleeding', 'yellow_urine', 'cramps', 'skin_peeling', 'swollen_legs',
           'history_of_alcohol_consumption', 'swelling_of_stomach', 'fast_heart_rate', 'enlarged_thyroid',
           'swollen_blood_vessels', 'blood_in_sputum', 'pain_in_anal_region', 'bloody_stool',
           'receiving_blood_transfusion', 'brittle_nails', 'lethargy', 'increased_appetite', 'drying_and_tingling_lips',
           'puffy_face_and_eyes', 'restlessness', 'sinus_pressure', 'swelled_lymph_nodes', 'palpitations',
           'irritability', 'redness_of_eyes', 'loss_of_smell', 'fluid_overload', 'mood_swings', 'cold_hands_and_feets',
           'runny_nose']

medical_conditions = {
    'Vertigo Paroxysmal Positional Vertigo': ['Otolaryngologist (ent)', 'Neurologist', 'Physical therapist',
                                              'General practitioner'],
    'AIDS': ['Internist', 'Family physician', 'Nurse practitioner', 'General practitioner'],
    'Acne': ['Dermatologist', 'Family physician', 'Nurse practitioner', 'General practitioner'],
    'Alcoholic hepatitis': ['Gastroenterologist', 'Hepatologist', 'Primary care doctor', 'General practitioner'],
    'Allergy': ['Allergist', 'Family physician', 'Internist', 'Nurse practitioner', 'General practitioner'],
    'Arthritis': ['Rheumatologist', 'Primary care doctor', 'Internist', 'Nurse practitioner', 'General practitioner'],
    'Bronchial Asthma': ['Pulmonologist', 'Allergist', 'Family physician', 'Nurse practitioner',
                         'General practitioner'],
    'Cervical spondylosis': ['Spine specialist', 'Neurosurgeon', 'Orthopedic surgeon', 'Physiatrist',
                             'General practitioner'],
    'Chicken pox': ['Primary care doctor/pediatrician', 'Dermatologist', 'Infectious disease specialist',
                    'General practitioner'],
    'Chronic cholestasis': ['Hepatologist', 'Primary care doctor', 'Internist', 'Nurse practitioner',
                            'General practitioner'],
    'Common Cold': ['Primary care doctor/pediatrician', 'Ear, nose, and throat (ent) doctor',
                    'Infectious disease specialist', 'General practitioner'],
    'Dengue': ['Primary care doctor/pediatrician', 'Infectious disease specialist', 'Hematologist',
               'General practitioner'],
    'Diabetes': ['Endocrinologist', 'Primary care doctor', 'Pediatrician', 'Nurse practitioner',
                 'General practitioner'],
    'Dimorphic hemorrhoids (piles)': ['Proctologist', 'Primary care doctor', 'Gastroenterologist', 'Nurse practitioner',
                                      'General practitioner'],
    'Drug Reaction': ['Allergist', 'Primary care doctor', 'Primary care doctor', 'Immunologist',
                      'General practitioner'],
    'Fungal infection': ['Dermatologist', 'Podiatrist', 'Infectious disease specialist', 'Primary care doctor',
                         'General practitioner'],
    'GERD': ['Gastroenterologist', 'Primary care doctor', 'Ear, nose, and throat (ent) doctor', 'General practitioner'],
    'Gastroenteritis': ['Gastroenterologist', 'Primary care doctor', 'Pediatrician', 'General practitioner'],
    'Heart attack': ['Cardiologist', 'Primary care doctor', 'Emergency room doctor', 'General practitioner'],
    'Hepatitis B': ['Primary care doctor', 'Infectious disease specialist', 'Hepatologist', 'General practitioner'],
    'Hepatitis C': ['Primary care doctor', 'Infectious disease specialist', 'Hepatologist', 'General practitioner'],
    'Hepatitis D': ['Primary care doctor', 'Infectious disease specialist', 'Hepatologist', 'Gastroenterologist',
                    'General practitioner'],
    'Hepatitis E': ['Primary care doctor', 'Hepatologist', 'Infectious disease specialist', 'General practitioner'],
    'Hypertension': ['Cardiologist', 'Primary care doctor', 'Nephrologist', 'General practitioner'],
    'Hyperthyroidism': ['Primary care doctor', 'Ear, nose, and throat (ent) doctor', 'Endocrinologist',
                        'General practitioner'],
    'Hypoglycemia': ['Endocrinologist', 'Primary care doctor', 'Diabetes educator', 'General practitioner'],
    'Hypothyroidism': ['Endocrinologist', 'Primary care doctor', 'Thyroidologist', 'General practitioner'],
    'Impetigo': ['Primary care doctor', 'Dermatologist', 'Pediatrician', 'General practitioner'],
    'Jaundice': ['Primary care doctor', 'Hepatologist', 'Gastroenterologist', 'General practitioner'],
    'Malaria': ['Infectious disease specialist', 'Primary care doctor', 'Travel medicine specialist',
                'General practitioner'],
    'Migraine': ['Neurologist', 'Primary care doctor', 'Ophthalmologist', 'General practitioner'],
    'Osteoarthristis': ['Rheumatologist', 'Primary care doctor', 'Orthopedist', 'General practitioner'],
    'Paralysis (brain hemorrhage)': ['Neurologist', 'Primary care doctor', 'Neurosurgeon', 'General practitioner'],
    'Peptic ulcer disease': ['Gastroenterologist', 'Primary care doctor', 'Internist', 'General practitioner'],
    'Pneumonia': ['Pulmonologist', 'Primary care doctor', 'Emergency room doctor', 'General practitioner'],
    'Psoriasis': ['Dermatologist', 'Primary care doctor', 'Rheumatologist', 'General practitioner'],
    'Tuberculosis': ['Pulmonologist', 'Infectious disease specialist', 'Primary care doctor', 'Emergency room doctor',
                     'General practitioner'],
    'Typhoid': ['Infectious disease specialist', 'Primary care doctor', 'Emergency room doctor',
                'General practitioner'],
    'Urinary tract infection': ['Urologist', 'Primary care doctor', 'Gynecologist', 'General practitioner'],
    'Varicose veins': ['Phlebologist', 'Vascular surgeon', 'Dermatologist', 'General practitioner',
                       'General practitioner']
}

symptom1 = symptom[:33]
symptom2 = symptom[33:66]
symptom3 = symptom[66:99]
symptom4 = symptom[99:]
l = [0] * 132
diseases = {0: '(vertigo) Paroymsal  Positional Vertigo', 1: 'AIDS', 2: 'Acne', 3: 'Alcoholic hepatitis',
            4: 'Allergy', 5: 'Arthritis', 6: 'Bronchial Asthma', 7: 'Cervical spondylosis', 8: 'Chicken pox',
            9: 'Chronic cholestasis', 10: 'Common Cold', 11: 'Dengue', 12: 'Diabetes ',
            13: 'Dimorphic hemmorhoids(piles)', 14: 'Drug Reaction', 15: 'Fungal infection', 16: 'GERD',
            17: 'Gastroenteritis', 18: 'Heart attack', 19: 'Hepatitis B', 20: 'Hepatitis C',
            21: 'Hepatitis D', 22: 'Hepatitis E', 23: 'Hypertension ', 24: 'Hyperthyroidism', 25: 'Hypoglycemia',
            26: 'Hypothyroidism',
            27: 'Impetigo', 28: 'Jaundice', 29: 'Malaria', 30: 'Migraine', 31: 'Osteoarthristis',
            32: 'Paralysis (brain hemorrhage)',
            33: 'Peptic ulcer diseae', 34: 'Pneumonia', 35: 'Psoriasis', 36: 'Tuberculosis', 37: 'Typhoid',
            38: 'Urinary tract infection', 39: 'Varicose veins', 40: 'hepatitis A'
            }

from account.decorators import login_first


@login_first
def re_home(request):
    return render(request, 'recommendation/re_home.html')


def recommend(request):
    # ml_model = joblib.load("../dr_re/ml_model/ml_model_whole.joblib")
    l = [0] * 132
    if request.method == 'POST':
        # when the form is submitted
        selected_symptom = request.POST.getlist('symptom')
        for i in selected_symptom:
            j = symptom.index(i)
            l[j] = 1
        # file_ = open(os.path.join(PROJECT_ROOT, 'filename'))
        # ml_model = joblib.load("../dr_re/ml_model/ml_model_new1.joblib")
        # # predictions = ml_model.predict(pd.DataFrame(l))
        # predictions = ml_model.predict(l)
        disease = ''
        if sum(l) == 0:
            disease = 'please select your symptom'
        else:
            # disease = ll[predictions.tolist()[0]]

            ml_model = joblib.load("../TELEHAKIM/dr_re/ml_model/ml_model_whole.joblib")
            # predictions = ml_model.predict  (pd.DataFrame(l))
            predictions = ml_model.predict(l)

            disease = diseases[predictions.tolist()[0]]

        return render(request, 'recommendation/recommend.html', {
            'symptom': symptom,
            'symptom1': symptom1,
            'symptom2': symptom2,
            'symptom3': symptom3,
            'symptom4': symptom4,
            'disease': disease,
            'sum': sum(l)})

    return render(request, "recommendation/recommend.html", {
        'symptom': symptom,
        'symptom1': symptom1,
        'symptom2': symptom2,
        'symptom3': symptom3,
        'symptom4': symptom4, })


def vom_interview(request):
    l[symptom.index("vomiting")] = 1
    return render(request, "recommendation/vomiting/vom_interview.html", {"list": l})


def interview3(request):
    return render(request, "recommendation/interview3.html")


def interview2(request):
    return render(request, "recommendation/interview2.html")


def interview0(request):
    return render(request, "recommendation/interview0.html", {})


def interview1(request):
    return render(request, "recommendation/interview1.html", {})


def interview4(request):
    return render(request, "recommendation/interview4.html")


symptom_list = ['cough']


def cough_interview1(request):
    return render(request, "recommendation/coughing/cough_interview1.html", {'symptom_list': symptom_list})


def cough_result(request):
    key_value = tuple(medical_conditions[request.GET.get('key')])
    doctors = list(
        Doctor.objects.filter(specialization__in=key_value).values('first_name', 'last_name', 'email', 'photo',
                                                                   'specialization'))

    context = {
        'doctors': doctors
    }
    return render(request, "recommendation/coughing/cough_result.html", context)


def cough_interview2(request):
    return render(request, "recommendation/coughing/cough_interview2.html")


# headache
def headache_interview1(request):
    return render(request, "recommendation/headache/headache_interview1.html")


def headache_interview2(request):
    return render(request, 'recommendation/headache/headache_interview2.html')


def headache_interview3(request):
    return render(request, 'recommendation/headache/headache_interview3.html')


def headache_interview4(request):
    return render(request, 'recommendation/headache/headache_interview4.html')


def headache_interview5(request):
    return render(request, 'recommendation/headache/headache_interview5.html')


def headache_result(request):
    key_value = tuple(medical_conditions[request.GET.get('key')])
    doctors = list(
        Doctor.objects.filter(specialization__in=key_value).values('first_name', 'last_name', 'email', 'photo',
                                                                   'specialization'))

    context = {
        'doctors': doctors
    }
    return render(request, "recommendation/headache/headache_result.html", context)


# fever
def fever_interview1(request):
    return render(request, "recommendation/fever/fever_interview1.html")


def fever_interview2(request):
    return render(request, "recommendation/fever/fever_interview2.html")


def fever_interview3(request):
    return render(request, "recommendation/fever/fever_interview3.html")


def fever_interview4(request):
    return render(request, "recommendation/fever/fever_interview4.html")


def fever_interview5(request):
    return render(request, "recommendation/fever/fever_interview5.html")


def fever_result(request):
    key_value = tuple(medical_conditions[request.GET.get('key')])
    doctors = list(
        Doctor.objects.filter(specialization__in=key_value).values('first_name', 'last_name', 'email', 'photo',
                                                                   'specialization'))

    context = {
        'doctors': doctors
    }
    return render(request, "recommendation/fever/fever_result.html", context)
