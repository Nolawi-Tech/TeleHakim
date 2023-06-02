from django.shortcuts import render
import pandas as pd
import joblib
import os
# from django.conf.settings import PROJECT_ROOT

from django.conf import settings

# Create your views here
# 
symptom = ['high_fever', 'nausea', 'skin_rash', 'yellowish_skin', 'itching', 'mild_fever', 'vomiting', 'fatigue', 'abnormal_menstruation', 'muscle_weakness', 'indigestion', 'joint_pain', 'yellowing_of_eyes', 'headache', 'blurred_and_distorted_vision', 'continuous_feel_of_urine', 'prominent_veins_on_calf', 'sweating', 'altered_sensorium', 'lack_of_concentration', 'neck_pain', 'abdominal_pain', 'irritation_in_anus', 'chills', 'shivering', 'sunken_eyes', 'breathlessness', 'hip_joint_pain', 'cough', 'ulcers_on_tongue', 'dark_urine', 'loss_of_appetite', 'weight_loss', 'irregular_sugar_level', 'malaise', 'rusty_sputum', 'chest_pain', 'mucoid_sputum', 'diarrhoea', 'family_history', 'phlegm', 'muscle_pain', 'congestion', 'patches_in_throat', 'loss_of_balance', 'unsteadiness', 'stomach_pain', 'spotting_ urination', 'dizziness', 'dischromic _patches', 'inflammatory_nails', 'acidity', 'stiff_neck', 'extra_marital_contacts', 'red_sore_around_nose', 'anxiety', 'scurring', 'burning_micturition', 'toxic_look_(typhos)', 'dehydration', 'blackheads', 'pain_during_bowel_movements', 'nodal_skin_eruptions', 'belly_pain', 'knee_pain', 'back_pain', 'coma', 'excessive_hunger', 'pus_filled_pimples', 'muscle_wasting', 'blister', 'pain_behind_the_eyes', 'receiving_unsterile_injections', 'continuous_sneezing', 'silver_like_dusting', 'depression', 'spinning_movements', 'swollen_extremeties', 'yellow_crust_ooze', 'weakness_in_limbs', 'passage_of_gases', 'polyuria', 'painful_walking', 'red_spots_over_body', 'constipation', 'bladder_discomfort', 'slurred_speech', 'small_dents_in_nails', 'obesity', 'distention_of_abdomen', 'watering_from_eyes', 'weakness_of_one_body_side', 'internal_itching', 'throat_irritation', 'swelling_joints', 'fluid_overload.1', 'acute_liver_failure', 'visual_disturbances', 'bruising', 'foul_smell_of urine', 'movement_stiffness', 'weight_gain', 'stomach_bleeding', 'yellow_urine', 'cramps', 'skin_peeling', 'swollen_legs', 'history_of_alcohol_consumption', 'swelling_of_stomach', 'fast_heart_rate', 'enlarged_thyroid', 'swollen_blood_vessels', 'blood_in_sputum', 'pain_in_anal_region', 'bloody_stool', 'receiving_blood_transfusion', 'brittle_nails', 'lethargy', 'increased_appetite', 'drying_and_tingling_lips', 'puffy_face_and_eyes', 'restlessness', 'sinus_pressure', 'swelled_lymph_nodes', 'palpitations', 'irritability', 'redness_of_eyes', 'loss_of_smell', 'fluid_overload', 'mood_swings', 'cold_hands_and_feets', 'runny_nose']
symptom_52 =["high_fever","nausea","skin_rash","yellowish_skin",
                    "itching","mild_fever","vomiting","fatigue",
                    "abnormal_menstruation","muscle_weakness","indigestion",
                    "joint_pain","yellowing_of_eyes","headache","blurred_and_distorted_vision",
                    "continuous_feel_of_urine","prominent_veins_on_calf","sweating", 
                    "altered_sensorium","lack_of_concentration","neck_pain",
                    "irritation_in_anus","abdominal_pain","chills",'shivering','sunken_eyes','breathlessness',
                     'hip_joint_pain','cough','ulcers_on_tongue','dark_urine','loss_of_appetite',
                     'weight_loss','irregular_sugar_level','malaise','rusty_sputum','chest_pain','mucoid_sputum',
                     'diarrhoea','family_history','phlegm','muscle_pain','congestion','patches_in_throat',
                     'unsteadiness','loss_of_balance','stomach_pain','spotting_ urination','dischromic _patches',
                    'dizziness','inflammatory_nails','acidity']
symptom1= symptom[:33]
symptom2= symptom[33:66]
symptom3= symptom[66:99]
symptom4= symptom[99:]
l=[0]*132
diseases={0: '(vertigo) Paroymsal  Positional Vertigo',1: 'AIDS',2: 'Acne',3: 'Alcoholic hepatitis',
         4: 'Allergy',5: 'Arthritis',6: 'Bronchial Asthma',7: 'Cervical spondylosis',8: 'Chicken pox',
         9: 'Chronic cholestasis',10: 'Common Cold',11: 'Dengue',12: 'Diabetes ',
        13: 'Dimorphic hemmorhoids(piles)',14: 'Drug Reaction',15: 'Fungal infection',16: 'GERD',
        17: 'Gastroenteritis',18: 'Heart attack',19: 'Hepatitis B',20: 'Hepatitis C',
        21: 'Hepatitis D',22: 'Hepatitis E',23: 'Hypertension ',24: 'Hyperthyroidism',25: 'Hypoglycemia',26: 'Hypothyroidism',
        27: 'Impetigo',28: 'Jaundice',29: 'Malaria',30: 'Migraine',31: 'Osteoarthristis',32: 'Paralysis (brain hemorrhage)',
        33: 'Peptic ulcer diseae',34: 'Pneumonia',35: 'Psoriasis',36: 'Tuberculosis',37: 'Typhoid',
        38: 'Urinary tract infection',39: 'Varicose veins',40: 'hepatitis A'}

def login(request):
     return render(request,'login.html')

def re_home(request):
     x=[1,2,3,4]
     
     return render(request,'recommendation/re_home.html',{"x":x})


def recommend(request):
     # ml_model = joblib.load("../dr_re/ml_model/ml_model_whole.joblib")
     
     if request.method == 'POST':
          # when the form is submitted
          selected_symptom = request.POST.getlist('symptom')
          for i in selected_symptom:
               j=symptom.index(i)
               l[j]=1
          # file_ = open(os.path.join(PROJECT_ROOT, 'filename'))
          # ml_model = joblib.load("../dr_re/ml_model/ml_model_new1.joblib")
          # # predictions = ml_model.predict(pd.DataFrame(l))
          # predictions = ml_model.predict(l)
          
          # disease = ll[predictions.tolist()[0]]
          
          ml_model = joblib.load("../TELEHAKIM/dr_re/ml_model/ml_model_whole.joblib")
          # predictions = ml_model.predict  (pd.DataFrame(l))
          predictions = ml_model.predict(l)
          
          disease = diseases[predictions.tolist()[0]]
          print (predictions) 
          return render(request, 'recommendation/recommend.html', {
               'symptom': symptom,
               'symptom1': symptom1,
               'symptom2': symptom2,
               'symptom3': symptom3,
               'symptom4': symptom4,
               'disease': disease})

     return render(request, "recommendation/recommend.html",{
          'symptom': symptom,
          'symptom1': symptom1,
          'symptom2': symptom2,
          'symptom3': symptom3,
          'symptom4': symptom4,})



def vom_interview(request):
     l[symptom.index("vomiting")]=1
     return render(request,"recommendation/vomiting/vom_interview.html",{"list":l})

def interview3(request):
     return render(request,"recommendation/interview3.html")
def interview2(request):
     return render(request,"recommendation/interview2.html")
def interview0(request):
     return render(request,"recommendation/interview0.html",{})
def interview1(request):
     return render(request,"recommendation/interview1.html",{})
def interview4(request):
     return render(request,"recommendation/interview4.html")
def cough_interview1(request):
     l[symptom.index("cough")]=1
     return render(request,"recommendation/coughing/cough_interview1.html")