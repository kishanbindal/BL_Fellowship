"""
    @Summary Address Book Driver Program

    @Author Kishan Bindal

    @Since December 2019
"""
from oop import addressbook


class AddBook:

    def main(self):

        ab = addressbook.AddressBook("ab.json")  # Create Address Book obj
        ab.open()  # Open Address Book
        print("\t ADDRESS BOOK\n\n\t\tOptions")
        print("1. Add New Entry\n2. Edit an Existing Entry\n3. Delete an Existing Entry"
              "\n4. Search for an Entry\n5. Display Entries\n6. Save\n7. Exit")
        while True:
            user_choice = int(input("\nPlease Select an action (1-7) : "))
            if user_choice == 1:
                ab.add_person()
            elif user_choice == 2:
                ab.edit_person()
            elif user_choice == 3:
                ab.delete_entry()
            elif user_choice == 4:
                first = input("Enter First Name of Entry to Search")  # First name to search
                last = input("Enter Last Name of Entry to Search")  # Last name to search
                print(ab.search_entries(first, last))
            elif user_choice == 5:
                ab.display_entries()
            elif user_choice == 6:
                ab.save()
            else:
                break


# Driver Code for address book
if __name__ == '__main__':
    a = AddBook()
    a.main()
