import json

# Load credit score data
with open("data/credit_scores.json", "r") as file:
    credit_scores = json.load(file)


def get_credit_score(phone: str):

    for record in credit_scores:

        if record["phone"] == phone:
            return record

    return {"message": "Credit score not found"}