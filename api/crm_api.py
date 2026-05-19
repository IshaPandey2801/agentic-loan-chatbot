import json

# Load customer data
with open("data/customers.json", "r") as file:
    customers = json.load(file)


def get_customer_by_phone(phone: str):

    for customer in customers:

        if customer["phone"] == phone:
            return customer

    return {"message": "Customer not found"}