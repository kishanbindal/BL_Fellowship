from oop import clinic


class ClDriver(clinic.Clinic):

    def __init__(self):
        clinic.Clinic.__init__(self)

    def _search_doctors(self):
        print("-----------DOCTOR SUBMENU--------------")
        print("""\t\t1. Search Doctor with Name
        2. Search Doctor with ID
        3. Search Doctor with Specialization
        4. Search Doctor by Availability
        5. Exit Submenu""")
        while True:
            while True:
                try:
                    user_choice = int(input("\nWhat would you like to do?"))
                except ValueError:
                    print("Values Must be Integers in range (1-5) Only!")
                else:
                    break
            if user_choice == 1:
                print(self.search_doctor_name())
            elif user_choice == 2:
                print(self.search_doctor_id())
            elif user_choice == 3:
                print(self.search_doctor_specialization())
            elif user_choice == 4:
                print(self.search_doctor_availability())
            else:
                print("EXIT BACK TO OPTIONS\n")
                break

    def search_patients(self):
        print("---------PATIENT SUBMENU------------")
        print("""\t\t1. Search Patient by name
        2. Search Patient by mobile number
        3. Search Patient by ID
        4. Exit""")
        while True:
            while True:
                try:
                    user_choice = int(input("\nWhat would you like to do?"))
                except ValueError:
                    print("Values Must be Integers in range (1-3) Only!")
                else:
                    break
            if user_choice == 1:
                print(self.search_patient_name())
            elif user_choice == 2:
                print(self.search_patient_number())
            elif user_choice == 3:
                print(self.search_patient_id())
            else:
                print("----------EXIT BACK TO OPTIONS-----------\n")
                break

    def main(self):
        print("--------------WELCOME TO THE CLINIC APP-----------------\n")
        print("\t\t\t\t OPTIONS")
        print("""\t\t1. Search For Doctor
        2. Search For Patient 
        3. Book Patient Appointment
        4. ShowDoctor Patient Report
        5. Exit""")
        while True:
            while True:
                try:
                    user_menu_choice = int(input("\nEnter Choice for menu(1-5) :"))
                except ValueError:
                    print("Integer Values, Values must be between 1 and 5 only!")
                else:
                    break
            if user_menu_choice == 1:
                self._search_doctors()
            elif user_menu_choice == 2:
                self.search_patients()
            elif user_menu_choice == 3:
                self.book_appointment()
            elif user_menu_choice == 4:
                self.display_doctor_patient_report()
            else:
                break


if __name__ == '__main__':
    cl = ClDriver()
    cl.main()
