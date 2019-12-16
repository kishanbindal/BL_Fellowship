"""
    @Summary Address Book to save,edit,delete and view Address book entries in .json file

    @Author Kishan Bindal

    @Since December 2019
"""
import json


class AddressBook:

    def __init__(self, file=None):
        self.file = file
        self.data = None

    def open(self):  # To Open Address book json file and store data
        with open(self.file) as f:
            self.data = json.load(f)

    def add_person(self):  # Add Person to Address Book
        while True:
            try:
                user_fname = input("Please enter First Name :\n")
                user_lname = input("Please Enter Last Name :\n")
                user_address = input("Please Enter Address :\n")
                user_city = input("Please Enter City :\n")
                user_state = input("Please Enter State :\n")
                user_zip = int(input("Please Enter Zip Code :\n"))
                user_phone = int(input("Please Enter Phone Number :\n"))
            except ValueError:
                print("Enter Name, Address, City and State as Strings."
                      "\nEnter Zip and Phone Numbers as Integer Values only.")
            else:
                break

        user_data = dict()  # Creating a dictionary to keep details of new entry
        user_data['fname'] = user_fname
        user_data['lname'] = user_lname
        user_data['address'] = user_address
        user_data['city'] = user_city
        user_data['state'] = user_state
        user_data['zip'] = user_zip
        user_data['phone'] = user_phone
        self.data['addressbook'].append(user_data)  # Adding dictionary to data

    def edit_person(self):  # Editing a person's details (Other than <FIRSTNAME> and <LASTNAME>
        print("-------EDIT--------")
        user_fname = input("\nEnter First Name of User who's entry you would like to update :\n")
        user_lname = input("\nEnter Last Name of User who's entry you would like to update :\n")
        if self.search_entries(user_fname, user_lname) is True:  # Check if person exists in AddressBook
            for item in self.data['addressbook']:
                # Checking for if both first name and last name point to the same item
                if (user_fname == item['fname']) and (user_lname == item['lname']):
                    print('What Parameter would you like to update? \n')
                    print("1. Address\n2. City\n3. State\n4. Zip\n5. Phone\n")
                    user_choice = int(input("Please choose number 1-5 to update : \t"))
                    if user_choice in range(1, 5):
                        user_addr = input("\nPlease Updated Enter Address :")
                        user_city = input("\nPlease Updated Enter City : ")
                        user_state = input("\nPlease Updated Enter State : ")
                        user_zip = int(input("\nEnter Updated Zip Code :"))
                        # Re-assigning Values to self.data since we are editing
                        item['address'], item['city'], item['state'] = user_addr, user_city, user_state
                        item['zip'] = user_zip
                    elif user_choice == 5:
                        user_phone = int(input("Please Enter Updated Phone Number :"))
                        item['phone'] = user_phone
                    elif user_choice == 6:
                        break
                    else:
                        print('Enter Valid Option')
        else:
            print("ENTRY NOT FOUND!!")  # Entry not found if self.search_entry = False

    def delete_entry(self):  # Delete Entry From AddressBook
        print("------Delete-------")
        user_fname = input("Enter First Name of Entry you would like to Delete :")
        user_lname = input("Enter Last Name of Entry you would like to Delete :")
        count = 0
        if self.search_entries(user_fname, user_lname) is True:  # Felete possible only when Person exists in AddBook
            for item in self.data['addressbook']:
                # First name and Last need to point to same person
                if (user_lname == item['lname']) and (user_fname == item['fname']):
                    del (self.data['addressbook'][count])
                else:
                    count += 1
        else:
            print("ENTRY NOT FOUND!!")  # If person does not exist in AddressBook entries

    def display_entries(self):  # To Display entries in AddressBook
        print("\n\tEntries\n")
        for item in self.data['addressbook']:
            print(f"Name : {item['fname']} {item['lname']}")
            print(f"Address : {item['address']}\nCity : {item['city']}\nState : {item['state']}")
            print(f"Zip : {item['zip']}\nPhone : {item['phone']}\n")

    # To search if person exists in AddressBook
    def search_entries(self, user_fname, user_lname):  # True if yes, False if no
        print("-----Search--------")
        for entry in self.data['addressbook']:
            if user_fname == entry['fname'] and user_lname == entry['lname']:
                return True
        return False

    def save(self):  # Save the Address Book back into json file
        with open(self.file, 'w') as f:
            json.dump(self.data, f, indent=2)
