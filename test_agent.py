from crewai import Task, Crew

from agents.sales_agent import sales_agent

# Create task
task = Task(
    description="""
    Talk to a customer who wants
    a personal loan of 5 lakh.
    """,

    expected_output="""
    A professional response asking
    for salary and tenure details.
    """,

    agent=sales_agent
)

# Create crew
crew = Crew(
    agents=[sales_agent],
    tasks=[task]
)

# Run crew
result = crew.kickoff()

print(result)