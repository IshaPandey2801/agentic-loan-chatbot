import math


def calculate_emi(
    principal,
    annual_interest_rate,
    tenure_months
):

    monthly_rate = annual_interest_rate / (12 * 100)

    emi = (
        principal
        * monthly_rate
        * math.pow(1 + monthly_rate, tenure_months)
    ) / (
        math.pow(1 + monthly_rate, tenure_months) - 1
    )

    return round(emi, 2)