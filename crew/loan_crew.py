from crewai import Crew

from agents.sales_agent import sales_agent
from agents.verification_agent import verification_agent
from agents.underwriting_agent import underwriting_agent
from agents.sanction_agent import sanction_agent

from tasks.loan_tasks import (
    sales_task,
    verification_task,
    underwriting_task,
    sanction_task
)

loan_crew = Crew(
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