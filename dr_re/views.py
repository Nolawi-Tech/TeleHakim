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

disease_sym = {
'vertigo (Paroxysmal Positional Vertigo)': ['vomiting', 'nausea', 'headache', 'loss_of_balance', 'spinning_movements', 'unsteadiness'],
'AIDS': ['extra_marital_contacts', 'muscle_wasting', 'high_fever', 'patches_in_throat'],
'Acne': ['blackheads', 'pus_filled_pimples', 'skin_rash', 'scarring'],
'Alcoholic hepatitis': ['vomiting', 'yellowish_skin', 'fluid_overload.1', 'abdominal_pain', 'distention_of_abdomen', 'swelling_of_stomach', 'history_of_alcohol_consumption'],
'Allergy': ['continuous_sneezing', 'chills', 'watering_from_eyes', 'shivering'],
'Arthritis': ['movement_stiffness', 'muscle_weakness', 'swelling_joints', 'stiff_neck', 'painful_walking'],
'Bronchial Asthma': ['mucoid_sputum', 'family_history', 'breathlessness', 'cough', 'high_fever', 'fatigue'],
'Cervical spondylosis': ['weakness_in_limbs', 'dizziness', 'loss_of_balance', 'neck_pain', 'back_pain'],
'Chicken pox': ['skin_rash', 'headache', 'loss_of_appetite', 'malaise', 'lethargy', 'itching', 'high_fever', 'mild_fever', 'swelled_lymph_nodes', 'fatigue', 'red_spots_over_body'],
'Chronic cholestasis': ['vomiting', 'yellowish_skin', 'nausea', 'loss_of_appetite', 'itching', 'abdominal_pain', 'yellowing_of_eyes'],
'Common Cold': ['throat_irritation', 'continuous_sneezing', 'sinus_pressure', 'headache', 'malaise', 'cough', 'phlegm', 'redness_of_eyes', 'high_fever', 'swelled_lymph_nodes', 'runny_nose', 'congestion', 'chills', 'loss_of_smell', 'muscle_pain', 'fatigue', 'chest_pain'],
'Dengue': ['vomiting', 'skin_rash', 'nausea', 'headache', 'loss_of_appetite', 'pain_behind_the_eyes', 'malaise', 'back_pain', 'fatigue', 'high_fever', 'red_spots_over_body', 'chills', 'muscle_pain', 'joint_pain'],
'Diabetes': ['irregular_sugar_level', 'restlessness', 'lethargy', 'obesity', 'blurred_and_distorted_vision', 'polyuria', 'weight_loss', 'excessive_hunger', 'fatigue', 'increased_appetite'],
'Dimorphic hemmorhoids(piles)': ['irritation_in_anus', 'constipation', 'bloody_stool', 'pain_during_bowel_movements', 'pain_in_anal_region'],
'Drug Reaction': ['skin_rash', 'stomach_pain', 'burning_micturition', 'itching', 'spotting_ urination'],
'Fungal infection': ['itching', 'nodal_skin_eruptions', 'skin_rash', 'dischromic_patches'],
'GERD': ['ulcers_on_tongue', 'vomiting', 'stomach_pain', 'acidity', 'cough', 'chest_pain'],
'Gastroenteritis': ['dehydration', 'sunken_eyes', 'vomiting', 'diarrhoea'],
'Heart attack': ['vomiting', 'chest_pain', 'breathlessness', 'sweating'],
'Hepatitis B': ['dark_urine', 'yellowish_skin', 'yellow_urine', 'loss_of_appetite', 'malaise', 'lethargy', 'receiving_unsterile_injections', 'itching', 'abdominal_pain', 'yellowing_of_eyes', 'fatigue', 'receiving_blood_transfusion'],
'Hepatitis C': ['family_history', 'nausea', 'yellowish_skin', 'loss_of_appetite', 'yellowing_of_eyes', 'fatigue'],
'Hepatitis D': ['dark_urine', 'vomiting', 'yellowish_skin', 'nausea', 'loss_of_appetite', 'abdominal_pain', 'yellowing_of_eyes', 'fatigue', 'joint_pain'],
'Hepatitis E': ['dark_urine', 'vomiting', 'coma', 'yellowish_skin', 'nausea', 'loss_of_appetite', 'abdominal_pain', 'high_fever', 'yellowing_of_eyes', 'fatigue', 'acute_liver_failure', 'joint_pain', 'stomach_bleeding'],
'Hypertension': ['dizziness', 'headache', 'loss_of_balance', 'lack_of_concentration', 'chest_pain'],
'Hyperthyroidism': ['abnormal_menstruation', 'sweating', 'mood_swings', 'muscle_weakness', 'restlessness', 'irritability', 'diarrhoea', 'weight_loss', 'excessive_hunger', 'fatigue', 'fast_heart_rate'],
'Hypoglycemia': ['slurred_speech', 'vomiting', 'drying_and_tingling_lips', 'sweating', 'nausea', 'headache', 'irritability', 'anxiety', 'blurred_and_distorted_vision', 'excessive_hunger', 'fatigue', 'palpitations'],
'Hypothyroidism': ['abnormal_menstruation', 'cold_hands_and_feets', 'dizziness', 'mood_swings', 'depression', 'lethargy', 'swollen_extremeties', 'irritability', 'brittle_nails', 'weight_gain', 'fatigue', 'puffy_face_and_eyes', 'enlarged_thyroid'],
'Impetigo': ['skin_rash', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze', 'high_fever'],
'Jaundice': ['dark_urine', 'vomiting', 'yellowish_skin', 'itching', 'abdominal_pain', 'high_fever', 'weight_loss', 'fatigue'],
'Malaria': ['vomiting', 'sweating', 'nausea', 'headache', 'diarrhoea', 'high_fever', 'chills', 'muscle_pain'],
'Migraine': ['visual_disturbances', 'acidity', 'headache', 'depression', 'irritability', 'blurred_and_distorted_vision', 'indigestion', 'stiff_neck', 'excessive_hunger'],
'Osteoarthristis': ['swelling_joints', 'neck_pain', 'knee_pain', 'hip_joint_pain', 'painful_walking', 'joint_pain'],
'Paralysis (brain hemorrhage)': ['weakness_of_one_body_side', 'vomiting', 'altered_sensorium', 'headache'],
'Peptic ulcer diseae': ['vomiting', 'passage_of_gases', 'loss_of_appetite', 'internal_itching', 'abdominal_pain', 'indigestion'],
'Pneumonia': ['sweating', 'malaise', 'rusty_sputum', 'breathlessness', 'cough', 'phlegm', 'high_fever', 'chills', 'fast_heart_rate', 'fatigue', 'chest_pain'],
'Psoriasis': ['skin_rash', 'silver_like_dusting', 'skin_peeling', 'small_dents_in_nails', 'inflammatory_nails', 'joint_pain'],
'Tuberculosis': ['vomiting', 'sweating', 'blood_in_sputum', 'loss_of_appetite', 'malaise', 'breathlessness', 'cough', 'phlegm', 'high_fever', 'weight_loss', 'mild_fever', 'yellowing_of_eyes', 'chills', 'swelled_lymph_nodes', 'fatigue', 'chest_pain'],
'Typhoid': ['toxic_look_(typhos)', 'fatigue', 'abdominal_pain', 'high_fever', 'belly_pain', 'headache', 'vomiting', 'chills', 'nausea', 'diarrhoea', 'constipation'],
'Urinary tract infection': ['burning_micturition', 'continuous_feel_of_urine', 'bladder_discomfort', 'foul_smell_of urine'],
'Varicose veins': ['fatigue', 'swollen_blood_vessels', 'prominent_veins_on_calf', 'swollen_legs', 'bruising', 'obesity', 'cramps']}






medical_conditions = {
    'Vertigo (Paroxysmal Positional Vertigo)': ['Otolaryngologist (ent)', 'Neurologist', 'Physical therapist',
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

@login_first
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

@login_first
def vom_interview(request):
    l[symptom.index("vomiting")] = 1
    return render(request, "recommendation/vomiting/vom_interview.html", {"list": l})

@login_first
def interview3(request):
    return render(request, "recommendation/interview3.html")

@login_first
def interview2(request):
    return render(request, "recommendation/interview2.html")

@login_first
def interview0(request):
    return render(request, "recommendation/interview0.html", {})

@login_first
def interview1(request):
    return render(request, "recommendation/interview1.html", {})

@login_first
def interview4(request):
    return render(request, "recommendation/interview4.html")


symptom_list = ['cough']

@login_first
def cough_interview1(request):
    return render(request, "recommendation/coughing/cough_interview1.html", {'symptom_list': symptom_list})

@login_first
def cough_result(request):

    l = [0] * 132
    y=request.GET.get('key')
    
    if '_' in y:
        y=y.replace("_"," ")

        

    for i in disease_sym[y]:
        j = symptom.index(i)
        l[j] = 1
    
    ml_model = joblib.load("../TELEHAKIM/dr_re/ml_model/ml_model_whole.joblib")

    predictions = ml_model.predict(l)

    disease = diseases[predictions.tolist()[0]]
    print(disease)
    x=medical_conditions[disease]
    key_value = tuple(x)
    doctors = list(
        Doctor.objects.filter(specialization__in=key_value).values())

    context = {
        'doctors': doctors
    }
    return render(request, "recommendation/coughing/cough_result.html", context)

@login_first
def cough_interview2(request):
    return render(request, "recommendation/coughing/cough_interview2.html")


@login_first
def headache_interview1(request):
    return render(request, "recommendation/headache/headache_interview1.html")

@login_first
def headache_interview2(request):
    return render(request, 'recommendation/headache/headache_interview2.html')

@login_first
def headache_interview3(request):
    return render(request, 'recommendation/headache/headache_interview3.html')

@login_first
def headache_interview4(request):
    return render(request, 'recommendation/headache/headache_interview4.html')

@login_first
def headache_interview5(request):
    return render(request, 'recommendation/headache/headache_interview5.html')

@login_first
def headache_result(request):
    l = [0] * 132
    for i in disease_sym[request.GET.get('key')]:
        j = symptom.index(i)
        l[j] = 1
    
    ml_model = joblib.load("../TELEHAKIM/dr_re/ml_model/ml_model_whole.joblib")

    predictions = ml_model.predict(l)

    disease = diseases[predictions.tolist()[0]]
    print(disease)
    x=medical_conditions[disease]
    key_value = tuple(x)
    doctors = list(
        Doctor.objects.filter(specialization__in=key_value).values())

    context = {
        'doctors': doctors
    }
    return render(request, "recommendation/headache/headache_result.html", context)


@login_first
def fever_interview1(request):
    return render(request, "recommendation/fever/fever_interview1.html")

@login_first
def fever_interview2(request):
    return render(request, "recommendation/fever/fever_interview2.html")

@login_first
def fever_interview3(request):
    return render(request, "recommendation/fever/fever_interview3.html")

@login_first
def fever_interview4(request):
    return render(request, "recommendation/fever/fever_interview4.html")

@login_first
def fever_interview5(request):
    return render(request, "recommendation/fever/fever_interview5.html")

@login_first
def fever_result(request):
    l = [0] * 132
    y=request.GET.get('key')
    
    if '_' in y:
        y=y.replace("_"," ")
    for i in disease_sym[y]:
        j = symptom.index(i)
        l[j] = 1
    
    ml_model = joblib.load("../TELEHAKIM/dr_re/ml_model/ml_model_whole.joblib")

    predictions = ml_model.predict(l)

    disease = diseases[predictions.tolist()[0]]
    print(disease)
    x=medical_conditions[disease]
    key_value = tuple(x)
    doctors = list(
        Doctor.objects.filter(specialization__in=key_value).values())

    context = {
        'doctors': doctors
    }
    return render(request, "recommendation/fever/fever_result.html", context)
