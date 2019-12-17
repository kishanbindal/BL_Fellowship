from oop import doctor
from oop import patient
import numpy
import json


class Clinic:

    with open("clinicman.json", 'r') as f:
        data = json.load(f)

    def __init__(self):
        self.doctors = self.get_doctors()
        self.patients = self.get_patients()

    def get_doctors(self):
        doctor_list = []
        for item in self.data['doctors']:
            doctor_list.append(doctor.Doctor(item['name'], item['id'], item['specialization'], item['availability']))
        return doctor_list

    def get_patients(self):
        patient_list = []
        for item in self.data['patient']:
            patient_list.append(patient.Patient(item['name'], item['id'], item['number'], item['age']))
        return patient_list

    def search_doctor_name(self):
        user_choice = input("Please input doctor name :\t")
        for item in self.doctors:
            if user_choice == item.name:
                return True
        return False

    def search_doctor_id(self):
        user_choice = input("Please input doctor ID :\t")
        for item in self.doctors:
            if user_choice == item.i_d:
                return True
        return False

    def search_doctor_specialization(self):
        user_choice = input("Please input doctor specialization :\t")
        for item in self.doctors:
            if user_choice == item.spec:
                return True
        return False

    def search_doctor_availability(self):
        user_choice = float(input("Enter Appointment time :\t"))
        for item in self.doctors:
            for time in item.avail:
                if user_choice in list(numpy.arange(time[0], time[1]+1, 0.25)):
                    return True
        return False

    def search_patient_name(self):
        user_choice = input("Enter Patient's name you are searching for :\t")
        for item in self.patients:
            if user_choice == item.patient_name:
                return True
        return False

    def search_patient_number(self):
        user_choice = input("Enter Patient's mobile number you are searching for :\t")
        for item in self.patients:
            if user_choice == item.number:
                return True
        return False

    def search_patient_id(self):
        user_choice = input("Enter Patient's name you are searching for :\t")
        for item in self.patients:
            if user_choice == item.patient_id:
                return True
        return False

    def book_appointment(self):
        patient_appointment_name = input("\nEnter Patient's name for booking an appointment :\t")
        x = 0
        while x < len(self.patients):
            pat = self.patients[x]
            if patient_appointment_name == pat.patient_name:
                while True:
                    try:
                        doct_name = input("Enter Doctor's name for appointment :\t")
                        a_t = float(input("Enter Appointment Time :"))
                    except ValueError:
                        print("Enter string values for doctor name and float/int times for appointment time")
                    else:
                        break
                for doc in self.doctors:
                    for ava in doc.avail:
                        if (doct_name == doc.name and a_t in list(numpy.arange(ava[0], ava[1] + 1, 0.25))) and \
                                doc.number_of_appointments_shift1 <= 5:
                            print(f"Appointment with {doc.name} is confirmed\nThank You")
                            doc.number_of_appointments_shift1 += 1
                        else:
                            if doc.number_of_appointments_shift2 <= 5:
                                print('Evening Appointment Available')
            x += 1


clinic = Clinic()
print(clinic.data)
clinic.book_appointment()

