"""
    @Summary Adding items to inventory

    @Author Kishan Bindal

    @Since December 2019
"""
import json


class InventoryManager:

    def __init__(self, file):  # Initialising instance variables, taking in a file to get data from json file
        self.file = file
        self.inventory = None

    def inventory_factory(self):  # Function to get data from inventory file and show value of each item in inventory
        with open(self.file, 'r') as f:
            self.inventory = json.load(f)
        for item in self.inventory["inventory"]:
            print(f"value of {item['weight']}Kg of {item['name']} is {item['weight'] * item['priceperkg']} ")

    def add_to_inventory(self):  # Function to add item to inventory and save to json file
        n = int(input("Enter number of items you would like to add to inventory :\n"))
        for i in range(n):
            while True:
                try:  # Getting information about data to add to inventory json file
                    n = input("Item you would want to enter to inventory :\n")
                    w = float(input("Enter weight of the product you are adding to inventory :\n"))
                    ppk = float(input("Enter cost per KG of the product "))

                except ValueError:
                    print("Please enter Only int/float values for weight and price per kg")

                else:
                    break

            with open(self.file, 'r+') as f:  # Saving changes to json file
                data = dict()
                data['name'] = n
                data['weight'] = w
                data['priceperkg'] = ppk
                self.inventory["inventory"].append(data)
                json.dump(self.inventory, f, indent=2)


if __name__ == "__main__":
    im = InventoryManager("inven.json")
    im.inventory_factory()
    im.add_to_inventory()
