from crewai import Agent

from config.settings import llm

master_agent = Agent(
    role="Loan Processing Manager",

    goal="""
    Coordinate all loan processing agents
    and manage the complete customer workflow.
    """,

    backstory="""
    You are the master coordinator of an NBFC loan system.
    You manage sales, verification,
    underwriting, and sanction workflows.
    """,

    llm=llm,

    verbose=True
)