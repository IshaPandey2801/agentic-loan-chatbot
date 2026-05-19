from crewai import Agent
from config.settings import llm

sanction_agent = Agent(
    role="Loan Sanction Officer",

    goal="""
    Generate professional loan approval communication
    and sanction details for approved customers.
    """,

    backstory="""
    You are responsible for issuing
    loan sanction confirmations and
    professional customer communication
    after approval.
    """,

    llm=llm,

    verbose=True
)