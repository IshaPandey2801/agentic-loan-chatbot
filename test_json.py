import json

with open("data/customers.json", "r") as file:
    customers = json.load(file)

print(customers[0])