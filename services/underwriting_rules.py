from services.emi_calculator import calculate_emi


def get_interest_rate(credit_score):

    # Risk-based pricing

    if credit_score >= 800:
        return 10.5

    elif credit_score >= 750:
        return 11.5

    elif credit_score >= 700:
        return 13.5

    else:
        return 16.0


def evaluate_loan(
    credit_score,
    requested_loan,
    preapproved_limit,
    salary,
    tenure_months
):

    # ----------------------------------------
    # CREDIT SCORE CHECK
    # ----------------------------------------

    if credit_score < 700:

        return {
            "status": "REJECTED",
            "reason": "Credit score below 700"
        }

    # ----------------------------------------
    # LOAN ELIGIBILITY CHECK
    # ----------------------------------------

    if requested_loan > (2 * preapproved_limit):

        return {
            "status": "REJECTED",
            "reason": "Requested loan amount exceeds maximum eligible limit"
        }

    # ----------------------------------------
    # INTEREST RATE
    # ----------------------------------------

    interest_rate = get_interest_rate(credit_score)

    # ----------------------------------------
    # EMI CALCULATION
    # ----------------------------------------

    emi = calculate_emi(
        principal=requested_loan,
        annual_interest_rate=interest_rate,
        tenure_months=tenure_months
    )

    # ----------------------------------------
    # AFFORDABILITY CHECK
    # ----------------------------------------

    max_allowed_emi = salary * 0.5

    if emi > max_allowed_emi:

        return {
            "status": "REJECTED",
            "reason": "Loan rejected because EMI exceeds affordability threshold",
            "emi": emi,
            "interest_rate": interest_rate
        }

    # ----------------------------------------
    # INSTANT APPROVAL
    # ----------------------------------------

    if requested_loan <= preapproved_limit:

        foir = round((emi / salary) * 100, 2)

        return {
            "status": "APPROVED",
            "reason": "Instant approval within pre-approved limit",
            "emi": emi,
            "interest_rate": interest_rate,
            "foir": foir,
            "risk_category": "LOW RISK"
        }

    # ----------------------------------------
    # CONDITIONAL APPROVAL
    # ----------------------------------------

    foir = round((emi / salary) * 100, 2)

    risk_category = "MEDIUM RISK"

    if foir < 30:
        risk_category = "LOW RISK"
    
    elif foir > 45:
        risk_category = "HIGH RISK"

    return {
        "status": "APPROVED",
        "reason": "Approved after affordability checks",
        "emi": emi,
        "interest_rate": interest_rate,
        "foir": foir,
        "risk_category": risk_category
    }