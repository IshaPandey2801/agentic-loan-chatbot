from fastapi import FastAPI

from api.crm_api import get_customer_by_phone
from api.bureau_api import get_credit_score
from api.offer_api import get_offer

# Create FastAPI app
app = FastAPI(
    title="Agentic Loan Chatbot APIs",
    description="Mock APIs for NBFC Loan Processing",
    version="1.0"
)

# Home Route
@app.get("/")
def home():
    return {
        "message": "Loan Chatbot API Running Successfully"
    }


# CRM API
@app.get("/customer/{phone}")
def fetch_customer(phone: str):

    return get_customer_by_phone(phone)


# Credit Bureau API
@app.get("/credit-score/{phone}")
def fetch_credit_score(phone: str):

    return get_credit_score(phone)


# Offer API
@app.get("/offer/{phone}")
def fetch_offer(phone: str):

    return get_offer(phone)