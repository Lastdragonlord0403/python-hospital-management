import pickle 
import os
import zipfile

doctor_list = [
    {'name': 'Cybill Ambrosine', 'position': 'Vice doctor', 'dob': '1/2/1997', 'id': '979797', 'phone': '123456789'},
    {'name': 'Lionel Ezra', 'position': 'Head doctor', 'dob': '6/9/1969', 'id': '696969', 'phone': '234567890'},
    {'name': 'Tallulah Braxton', 'position': 'Vice doctor', 'dob': '3/2/1989', 'id': '898989', 'phone': '3456789098'}
]

nurse_list = [
    {'name': 'Maleah Skyler', 'position': 'Head nurse', 'dob': '4/7/1990', 'id': '909090'},
    {'name': 'Aaren Clifton', 'position': 'Vice nurse', 'dob': '6/7/1999', 'id': '999999'}
]

patient_list = [
    {'name': 'Praise Sorrel', 'condition': 'Post-traumatic stress disorder (PTSD)', 'dob': '12/10/1979'},
    {'name': 'Kortney Sage', 'condition': 'Psychosis', 'dob': '20/05/1987'},
    {'name': 'Claude Brittania', 'condition': 'Hepatitis C', 'dob': '20/08/1984'},
    {'name': 'Carver Darnell', 'condition': 'Psoriasis', 'dob': '25/01/1988'},
    {'name': 'Baker Emmalyn', 'condition': 'Restless legs syndrome', 'dob': '15/07/1971'}
]

def save_doctors(doctors_list):
    with open("doctors.pkl", "wb") as f:
        pickle.dump(doctors_list, f, pickle.HIGHEST_PROTOCOL)

def save_workers(workers_list):
    with open("workers.pkl", "wb") as f:
        pickle.dump(workers_list, f, pickle.HIGHEST_PROTOCOL)

def save_patients(patients_list):
    with open("patients.pkl", "wb") as f:
        pickle.dump(patients_list, f, pickle.HIGHEST_PROTOCOL)

def save_medicines(medicines_list):
    with open("medicines.pkl", "wb") as f:
        pickle.dump(medicines_list, f, pickle.HIGHEST_PROTOCOL)

def save_pa_doc(pa_doc_list):
    with open("pa_doc.pkl", "wb") as f:
        pickle.dump(pa_doc_list, f, pickle.HIGHEST_PROTOCOL)

def save_pa_med(pa_med_list):
    with open("pa_med.pkl", "wb") as f:
        pickle.dump(pa_med_list, f, pickle.HIGHEST_PROTOCOL)

def zip_data():
    with zipfile.ZipFile('hospital.dat', 'w', compression=zipfile.ZIP_DEFLATED) as zip:        
        zip.writestr('doctors.pkl', pickle.dumps(doctor_list))
        zip.writestr('workers.pkl', pickle.dumps(nurse_list))
        zip.writestr('patients.pkl', pickle.dumps(patient_list))
        zip.writestr('medicines.pkl', pickle.dumps([]))
        zip.writestr('pa_doc.pkl', pickle.dumps([]))
        zip.writestr('pa_med.pkl', pickle.dumps([]))
    os.remove('doctors.pkl')
    os.remove('workers.pkl')
    os.remove('patients.pkl')
    os.remove('medicines.pkl')
    os.remove('pa_doc.pkl')
    os.remove('pa_med.pkl')

#===========================================================================

def load_doctors():
    doctor_list = []
    if(os.path.exists("doctors.pkl")):
        with open("doctors.pkl", "rb") as f:
            doctor_list = pickle.load(f)

    return (doctor_list)

def load_workers():
    workers_list = []
    if(os.path.exists("workers.pkl")):
        with open("workers.pkl", "rb") as f:
            workers_list = pickle.load(f)

    return (workers_list)

def load_patients():
    patients_list = []
    if(os.path.exists("patients.pkl")):
        with open("patients.pkl", "rb") as f:
            patients_list = pickle.load(f)

    return (patients_list)

def load_medicines():
    medicines_list = []
    if(os.path.exists("medicines.pkl")):
        with open("medicines.pkl", "rb") as f:
            medicines_list = pickle.load(f)

    return (medicines_list)

def load_pa_doc():
    pa_doc_list = []
    if(os.path.exists("pa_doc.pkl")):
        with open("pa_doc.pkl", "rb") as f:
            pa_doc_list = pickle.load(f)

    return (pa_doc_list)

def load_pa_med():
    pa_med_list = []
    if(os.path.exists("pa_med.pkl")):
        with open("pa_med.pkl", "rb") as f:
            pa_med_list = pickle.load(f)

    return (pa_med_list)

def unzip_data():
    if os.path.exists('hospital.dat'):
        with zipfile.ZipFile('hospital.dat', 'r') as zip:
            zip.extractall()
        os.remove("hospital.dat")
