from oop import clinic


class ClDriver(clinic.Clinic):

    def __init__(self):
        clinic.Clinic.__init__(self)

    def _search_doctors(self):
        print("-----------DOCTOR SUBMENU--------------")
        print("1. Search Doctor with Name\n2. Search Doctor with ID\n3. Search Doctor with Specialization\n"
              "4. Search Doctor by Availability\n5. Exit Submenu")
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
                print("EXIT BACK TO OPTIONS")
                break

    def search_patients(self):
        print("---------PATIENT SUBMENU------------")
        print("\n1. Search Patient by name\n2. Search Patient by mobile number\n3. Search Patient by ID\n4. Exit")
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
                print("----------EXIT BACK TO OPTIONS-----------")
                break

    def main(self):
        print("--------------WELCOME TO THE CLINIC APP-----------------\n")
        print("\t\t\t\t\t OPTIONS")
        print("1. Search For Doctor\n2. Search For Patient\n3. Book Patient Appointment\n4. Show Doctor Patient Report")
        print("5. Exit")
        while True:
            while True:
                try:
                    user_menu_choice = int(input("\nEnter Choice for menu(1-5) :"))
                except ValueError:
                    print("Integer Values, Values must be between 1 and 5 only!")
                else:
                    break
            if user_menu_choice == 1:
                ClDriver()._search_doctors()
            elif user_menu_choice == 2:
                ClDriver().search_patients()
            elif user_menu_choice == 3:
                ClDriver().book_appointment()
            elif user_menu_choice == 4:
                ClDriver().display_doctor_patient_report()
            else:
                break


if __name__ == '__main__':
    cl = ClDriver
    cl.main(ClDriver())
