from crewai import Task

from agents.sales_agent import sales_agent
from agents.verification_agent import verification_agent
from agents.underwriting_agent import underwriting_agent
from agents.sanction_agent import sanction_agent


sales_task = Task(
    description="""
    Answer customer loan-related questions professionally.
    Help customers understand EMI, tenure,
    interest rates, and loan eligibility.
    """,

    expected_output="Helpful response to customer query.",

    agent=sales_agent
)


verification_task = Task(
    description="""
    Verify customer information,
    salary details,
    and uploaded document details.
    """,

    expected_output="Customer verification completed.",

    agent=verification_agent
)


underwriting_task = Task(
    description="""
    Analyze customer eligibility,
    FOIR,
    risk category,
    and loan approval chances.
    """,

    expected_output="Loan underwriting decision completed.",

    agent=underwriting_agent
)


sanction_task = Task(
    description="""
    Generate final customer communication
    regarding loan approval or rejection.
    """,

    expected_output="Professional sanction communication generated.",

    agent=sanction_agent
)