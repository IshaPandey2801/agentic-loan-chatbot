import json

# Load offer data
with open("data/offers.json", "r") as file:
    offers = json.load(file)


def get_offer(phone: str):

    for offer in offers:

        if offer["phone"] == phone:
            return offer

    return {"message": "Offer not found"}