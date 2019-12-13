import json

with open("inventorydetails", 'r') as f:
    inventory = json.load(f)

for item in inventory["inventory"]:
    print(f"value of {item['weight']}Kg of {item['name']} is {item['weight']*item['priceperkg']} ")

with open ("inven.json", 'w') as f:
    json.dump(inventory, f, indent=4)

print(json.dumps(inventory))