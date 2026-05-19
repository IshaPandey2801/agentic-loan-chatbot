from crewai import Task, Crew

from agents.master_agent import master_agent
from agents.sales_agent import sales_agent
from agents.verification_agent import verification_agent
from agents.underwriting_agent import underwriting_agent
from agents.sanction_agent import sanction_agent


def run_loan_workflow(customer_data):

    # -------------------------------
    # Sales Task
    # -------------------------------

    sales_task = Task(
        description=f"""
        Talk to customer and understand loan requirement.

        Customer Name: {customer_data['name']}
        Loan Amount: {customer_data['loan_amount']}
        Salary: {customer_data['salary']}
        Tenure: {customer_data['tenure']}
        """,

        expected_output="Customer loan requirement summary",

        agent=sales_agent
    )

    # -------------------------------
    # Verification Task
    # -------------------------------

    verification_task = Task(
        description=f"""
        Verify customer KYC details.

        Phone: {customer_data['phone']}
        City: {customer_data['city']}
        Address: {customer_data['address']}
        """,

        expected_output="Verification completed",

        agent=verification_agent
    )

    # -------------------------------
    # Underwriting Task
    # -------------------------------

    underwriting_task = Task(
        description=f"""
        Evaluate loan eligibility.

        Credit Score: {customer_data['credit_score']}
        Loan Amount: {customer_data['loan_amount']}
        Salary: {customer_data['salary']}
        """,

        expected_output="Loan approval or rejection decision",

        agent=underwriting_agent
    )

    # -------------------------------
    # Sanction Task
    # -------------------------------

    sanction_task = Task(
        description="""
        Generate sanction letter for approved customer.
        """,

        expected_output="Sanction letter generated",

        agent=sanction_agent
    )

    # -------------------------------
    # Crew
    # -------------------------------

    crew = Crew(
        agents=[
            master_agent,
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

    result = crew.kickoff()

    return result