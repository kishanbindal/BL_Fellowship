from oop import doctor
from oop import patient
import numpy
import json


class Clinic(patient.Patient, doctor.Doctor):

    with open("clinicman.json", 'r') as f:
        _data = json.load(f)

    def __init__(self):
        self._doctors = self.get_doctors()
        self._patients = self.get_patients()

    def get_doctors(self):
        doctor_list = []
        for item in self._data['doctors']:
            doctor_list.append(doctor.Doctor(item['name'], item['id'], item['specialization'], item['availability']))
        return doctor_list

    def get_patients(self):
        patient_list = []
        for item in self._data['patient']:
            patient_list.append(patient.Patient(item['name'], item['id'], item['number'], item['age']))
        return patient_list

    def search_doctor_name(self):
        user_choice = input("Please input doctor name :\t")
        for item in self._doctors:
            if user_choice == item._name:
                return True
        return False

    def search_doctor_id(self):
        user_choice = input("Please input doctor ID :\t")
        for item in self._doctors:
            if user_choice == item._i_d:
                return item._name
        return False

    def search_doctor_specialization(self):
        user_choice = input("Please input doctor specialization :\t")
        for item in self._doctors:
            if user_choice == item._spec:
                return item._name
        return False

    def search_doctor_availability(self):
        user_choice = float(input("Enter Appointment time :\t"))
        for item in self._doctors:
            for time in item._avail:
                if user_choice in list(numpy.arange(time[0], time[1]+1, 0.25)):
                    return item._name
        return False

    def search_patient_name(self):
        user_choice = input("Enter Patient's name you are searching for :\t")
        for item in self._patients:
            if user_choice == item.patient_name:
                return True
        return False

    def search_patient_number(self):
        user_choice = input("Enter Patient's mobile number you are searching for :\t")
        for item in self._patients:
            if user_choice == item.number:
                return True
        return False

    def search_patient_id(self):
        user_choice = input("Enter Patient's name you are searching for :\t")
        for item in self._patients:
            if user_choice == item.patient_id:
                return True
        return False

    def book_appointment(self):
        patient_appointment_name = input("\nEnter Patient's name for booking an appointment :\t")
        x = 0
        while x < len(self._patients):
            pat = self._patients[x]
            if patient_appointment_name == pat.patient_name:
                while True:
                    try:
                        doct_name = input("Enter Doctor's name for appointment :\t")
                        a_t = float(input("Enter Appointment Time :\t"))
                    except ValueError:
                        print("Enter string values for doctor name and float/int times for appointment time")
                    else:
                        break
                for doc in self._doctors:
                    if len(doc._avail) < 2 and doct_name == doc._name:
                        for t in doc._avail:
                            if (a_t in list(numpy.arange(t[0], t[1]+1, 0.25))) \
                                    and (doc.number_of_appointments_shift1 <= 5):
                                print(f"Appointment with {doc._name} confirmed\nThank You!!")
                                if a_t < 12:
                                    pat.appointment_time = f"{a_t} AM"
                                else:
                                    pat.appointment_time = f"{a_t} PM"
                                doc.number_of_appointments_shift1 += 1
                                doc.list_of_appointments.append(pat)
                            else:
                                print('No Appointments available, Try for another day.')
                                break
                    elif len(doc._avail) > 1 and doct_name == doc._name:
                        time = doc._avail
                        if a_t in list(numpy.arange(time[0][0], time[0][1]+0.25, 0.25)):
                            if doc.number_of_appointments_shift1 >= 5 > doc.number_of_appointments_shift2:
                                print('Evening Appointment Slot Available')
                                break
                            else:
                                print(f"Appointment with {doc._name} is confirmed.\nAppointment time : {a_t}"
                                      f"\nThank You")
                                if a_t < 12:
                                    pat.appointment_time = f"{a_t} AM"
                                else:
                                    pat.appointment_time = f"{a_t} PM"
                                doc.list_of_appointments.append(pat)
                                doc.number_of_appointments_shift1 += 1
                                break
                        elif doct_name == doc._name and a_t in list(numpy.arange(time[1][0], time[1][1]+0.25, 0.25)):
                            if doc.number_of_appointments_shift2 >= 5 > doc.number_of_appointments_shift1:
                                print('Morning Appointment Slot available.')
                                break
                            else:
                                print(f"Appointment with {doc._name} is confirmed.\nAppointment time : {a_t}"
                                      f"\nThank You")
                                if a_t < 12:
                                    pat.appointment_time = f"{a_t} AM"
                                else:
                                    pat.appointment_time = f"{a_t} PM"
                                doc.list_of_appointments.append(pat)
                                doc.number_of_appointments_shift2 += 1
                                break
            x += 1

    def display_popular_doctor(self):
        temp = self._doctors[0]
        for doc in self._doctors:
            if doc.total_appointments > temp.total_appointments:
                temp = doc
        print(f"\nMost Popular Doctor in clinic : \t\t{temp._name}")

    def display_popular_specialization(self):
        spec = dict()
        for doc in self._doctors:
            spec[doc._spec] = 0
            if doc.total_appointments > 0:
                spec[doc._spec] += 1
        m = max(spec, key=spec.get)
        print(f"Most Popular Specialization in Clinic :\t\t{m}")

    def display_doctor_patient_report(self):
        print("\nDoctor Name\t\tPatient Name\t\tPatient Appointment Time")
        for doc in self._doctors:
            for pat in doc.list_of_appointments:
                print(f"  {doc._name}\t\t\t{pat.patient_name}\t\t\t\t{pat.appointment_time}")


clinic = Clinic()
for i in range(2):
    clinic.book_appointment()
clinic.display_doctor_patient_report()
