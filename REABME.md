

#  Agentic AI Loan Assistant

An AI-powered multi-agent Personal Loan Assistant built using **CrewAI, Streamlit, FastAPI, and Python**.

This project simulates an NBFC (Non-Banking Financial Company) loan processing system where multiple AI agents collaborate to process customer loan applications, evaluate eligibility, calculate EMI, generate sanction letters, and provide intelligent loan guidance.



#  Features

##  AI Multi-Agent System
Built using CrewAI with specialized agents:

- Sales Agent
- Verification Agent
- Underwriting Agent
- Sanction Agent
- Master Coordination Agent



#  Functionalities

##  Customer Onboarding
- Existing customer lookup
- New customer registration
- Customer information collection

##  Loan Evaluation
- Credit score analysis
- FOIR calculation
- Risk categorization
- Eligibility verification
- Interest rate evaluation

##  EMI & Loan Analytics
- EMI calculation
- Loan tenure analysis
- Interest breakdown visualization
- Interactive analytics dashboard

##  AI Loan Chatbot
- AI-powered loan assistant
- Answers customer loan-related queries
- Provides guidance about:
  - EMI
  - Eligibility
  - Interest rates
  - Personal loans
  - Credit score

##  PDF Sanction Letter
- Automatic sanction letter generation
- Downloadable PDF format

##  Workflow Visualization
- AI workflow summary
- Agent activity tracking
- Loan processing stages



#  Tech Stack

## Frontend
- Streamlit

## Backend
- FastAPI
- Python

## AI Framework
- CrewAI
- Gemini API

## Data Processing
- Pandas
- NumPy

## Visualization
- Plotly

## PDF Generation
- FPDF



#  AI Agents

| Agent | Responsibility |
|------|----------------|
| Sales Agent | Handles customer loan queries |
| Verification Agent | Verifies customer details |
| Underwriting Agent | Evaluates eligibility and risk |
| Sanction Agent | Generates approval communication |
| Master Agent | Coordinates overall workflow |



# Project Structure

agentic-loan-chatbot/
│
├── agents/
├── api/
├── config/
├── crew/
├── data/
├── frontend/
├── services/
├── tasks/
├── test_agent.py
├── requirements.txt
├── README.md
└── .gitignore


#  Installation

##  Clone Repository
git clone https://github.com/IshaPandey2801/agentic-loan-chatbot


##  Move Into Project Folder
cd agentic-loan-chatbot


##  Create Virtual Environment
python -m venv venv


##  Activate Virtual Environment

### Windows
venv\Scripts\activate




#  Install Dependencies

pip install -r requirements.txt


#  Environment Variables

Create a `.env` file:

GEMINI_API_KEY=your_api_key_here




#  Run FastAPI Server

uvicorn api.main:app --reload




#  Run Streamlit App


streamlit run frontend/streamlit_app.py




##  Loan Application Interface

* Customer onboarding
* Salary slip upload
* Loan application form

##  Analytics Dashboard

* EMI analysis
* FOIR analysis
* Risk assessment

##  AI Chatbot

* Intelligent loan assistance
* Customer query handling



#  Future Enhancements

* OCR-based salary slip extraction
* Voice-enabled assistant
* WhatsApp integration
* Database integration
* Fraud detection AI
* RAG-based policy chatbot
* Cloud deployment
* Authentication system



#  Learning Outcomes

This project demonstrates:

* Generative AI
* Multi-Agent AI Systems
* Streamlit Development
* FastAPI APIs
* Financial AI Workflows
* Loan Underwriting Logic
* AI Chatbot Development
* PDF Automation
* Data Visualization



#  Author

Shreya Pandey

B.Tech Data Science Student
Passionate about Generative AI, NLP, and Machine Learning



# ⭐ If You Like This Project

Give this repository a ⭐ on GitHub.


