"""
    @Summary Driver Code for inventorymanager.py

    @Author Kishan Bindal

    @Since December 2019
"""
from oop import inventorymanager


def invenmanager():
    im = inventorymanager.InventoryManager("inven.json")
    print("\tOptions")
    print(f"1. View Inventory\n2. Add To Inventory\n3. Exit")
    while True:
        user_choice = int(input("Please enter Choice (1-3): \t"))
        if user_choice not in range(1, 4):
            raise ValueError("Enter Values between 1 and 3 only!")
        else:
            if user_choice == 1:
                im.inventory_factory()
            elif user_choice == 2:
                im.add_to_inventory()
            else:
                break


if __name__ == '__main__':
    invenmanager()
