from crewai import Task, Crew

# Agents
from agents.sales_agent import sales_agent
from agents.verification_agent import verification_agent
from agents.underwriting_agent import underwriting_agent
from agents.sanction_agent import sanction_agent

# APIs
from api.crm_api import get_customer_by_phone
from api.bureau_api import get_credit_score
from api.offer_api import get_offer

# Underwriting Rules
from services.underwriting_rules import evaluate_loan


# -----------------------------------
# CUSTOMER INPUT
# -----------------------------------

phone = "9876543210"

requested_loan = 500000

salary = 75000


# -----------------------------------
# FETCH CUSTOMER DATA
# -----------------------------------

customer = get_customer_by_phone(phone)

credit_data = get_credit_score(phone)

offer_data = get_offer(phone)

credit_score = credit_data["credit_score"]

preapproved_limit = offer_data["preapproved_limit"]


# -----------------------------------
# SALES TASK
# -----------------------------------

sales_task = Task(
    description=f"""
    Customer wants a personal loan of ₹{requested_loan}.

    Explain loan offerings professionally.
    Ask relevant loan questions.
    """,

    expected_output="""
    Professional loan sales response.
    """,

    agent=sales_agent
)


# -----------------------------------
# VERIFICATION TASK
# -----------------------------------

verification_task = Task(
    description=f"""
    Verify customer details:

    Name: {customer['name']}
    Phone: {customer['phone']}
    City: {customer['city']}
    Address: {customer['address']}
    """,

    expected_output="""
    Customer verification status.
    """,

    agent=verification_agent
)


# -----------------------------------
# UNDERWRITING DECISION
# -----------------------------------

decision = evaluate_loan(
    credit_score=credit_score,
    requested_loan=requested_loan,
    preapproved_limit=preapproved_limit,
    salary=salary
)


# -----------------------------------
# UNDERWRITING TASK
# -----------------------------------

underwriting_task = Task(
    description=f"""
    Analyze loan eligibility.

    Credit Score: {credit_score}

    Requested Loan: ₹{requested_loan}

    Pre-approved Limit: ₹{preapproved_limit}

    Underwriting Decision:
    {decision}
    """,

    expected_output="""
    Professional underwriting explanation.
    """,

    agent=underwriting_agent
)


# -----------------------------------
# SANCTION TASK
# -----------------------------------

sanction_task = Task(
    description=f"""
    Generate final customer communication.

    Final Decision:
    {decision}
    """,

    expected_output="""
    Professional approval/rejection response.
    """,

    agent=sanction_agent
)


# -----------------------------------
# CREATE CREW
# -----------------------------------

crew = Crew(
    agents=[
        sales_agent,
        verification_agent,
        underwriting_agent,
        sanction_agent
    ],

    tasks=[
        sales_task,
        verification_task,
        underwriting_task,
        sanction_task
    ],

    verbose=True
)


# -----------------------------------
# RUN WORKFLOW
# -----------------------------------

result = crew.kickoff()

print("\n")
print("===================================")
print("FINAL LOAN DECISION")
print("===================================")
print(decision)
print("\n")

print(result)