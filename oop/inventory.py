"""
    @Summary To Calculate value of inventory

    @Author Kishan Bindal

    @Since December 2019
"""
import json

with open("inventorydetails", 'r') as f:  # Open json File
    inventory = json.load(f)

for item in inventory["inventory"]:  # Function to calculate the value of inventory
    print(f"value of {item['weight']}Kg of {item['name']} is {item['weight']*item['priceperkg']} ")

with open ("inven.json", 'w') as f:  # Function to dump data into json file
    json.dump(inventory, f, indent=4)

