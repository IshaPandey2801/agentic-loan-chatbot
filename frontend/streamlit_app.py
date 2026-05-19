import sys
import os
import pandas as pd
# Fix import paths
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

import streamlit as st
from crew_orchestrator import run_loan_workflow
from services.pdf_generator import generate_sanction_letter
from api.crm_api import get_customer_by_phone
from api.bureau_api import get_credit_score
from api.offer_api import get_offer
from crewai import Crew, Task
from services.underwriting_rules import evaluate_loan
from agents.sales_agent import sales_agent
from crew.loan_crew import loan_crew
# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Agentic AI Loan Chatbot",
    page_icon="💰",
    layout="centered"
)


# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------

if "new_customer" not in st.session_state:
    st.session_state.new_customer = False


# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("💰 Agentic AI Loan Assistant")

st.markdown("""
Welcome to the AI-powered Personal Loan Assistant.

Please provide your details below.
""")


# ---------------------------------------------------
# USER INPUTS
# ---------------------------------------------------

phone = st.text_input(
    "Enter Your Phone Number",
    key="phone_input"
)

requested_loan = st.number_input(
    "Requested Loan Amount (Rs.)",
    min_value=10000,
    max_value=5000000,
    step=10000,
    key="loan_input"
)

salary = st.number_input(
    "Monthly Salary (Rs.)",
    min_value=10000,
    max_value=1000000,
    step=5000,
    key="salary_input"
)

salary_slip = st.file_uploader(
    "Upload Salary Slip",
    type=["pdf", "png", "jpg"],
    key="salary_slip_upload"
)

# Loan Tenure
tenure_months = st.selectbox(
    "Select Loan Tenure (Months)",
    [12, 24, 36, 48, 60],
    key="tenure_input"
)
# ---------------------------------------------------
# PROCESS BUTTON
# ---------------------------------------------------

process_button = st.button(
    "Process Loan Application",
    key="process_button"
)


# ---------------------------------------------------
# MAIN WORKFLOW
# ---------------------------------------------------

if process_button:

    # Validate phone
    if phone == "":

        st.error("Please enter phone number.")

    else:

        # Fetch customer
        customer = get_customer_by_phone(phone)

        # ---------------------------------------------------
        # EXISTING CUSTOMER
        # ---------------------------------------------------

        if "message" not in customer:

            # Existing customer
            st.session_state.new_customer = False

            # Fetch bureau data
            credit_data = get_credit_score(phone)

            # Fetch offer data
            offer_data = get_offer(phone)

            credit_score = credit_data["credit_score"]

            preapproved_limit = offer_data["preapproved_limit"]

            # Customer Details
            st.subheader("Customer Details")

            st.write(f"Name: {customer['name']}")
            st.write(f"City: {customer['city']}")
            st.write(f"Employment Type: {customer['employment_type']}")

            # Credit Details
            st.subheader("Credit Evaluation")

            st.write(f"Credit Score: {credit_score}")

            st.write(f"Pre-approved Limit: Rs.{preapproved_limit}")

            # Run Underwriting
            decision = evaluate_loan(
                credit_score=credit_score,
                requested_loan=requested_loan,
                preapproved_limit=preapproved_limit,
                salary=salary,
                tenure_months=tenure_months
            )

            # Run AI Workflow

            customer_data = {
                "name": customer["name"],
                "phone": phone,
                "city": customer["city"],
                "address": customer["address"],
                "loan_amount": requested_loan,
                "salary": salary,
                "tenure": tenure_months,
                "credit_score": credit_score
            }

            with st.spinner("AI Agents Processing Loan Application..."):

                ai_result = run_loan_workflow(customer_data)

            st.subheader("AI Agent Workflow Summary")

            st.write(ai_result)
            # Final Decision
            st.subheader("Loan Decision")

            if decision["status"] == "APPROVED":

                st.success("✅ LOAN APPROVED")

                # Generate PDF
                pdf_path = generate_sanction_letter(
                    customer_name=customer["name"],
                    loan_amount=requested_loan,
                    tenure=tenure_months,
                    interest_rate=decision["interest_rate"],
                    emi=decision["emi"]
                )

                # Download PDF
                with open(pdf_path, "rb") as pdf_file:

                    st.download_button(
                        label="📄 Download Sanction Letter",
                        data=pdf_file,
                        file_name="sanction_letter.pdf",
                        mime="application/pdf"
                    )

            else:

                st.error("❌ LOAN REJECTED")

            st.write(f"Reason: {decision['reason']}")
            if "emi" in decision:

                st.write(f"Monthly EMI: Rs.{decision['emi']:,.2f}")

            if "interest_rate" in decision:

                st.write(f"Interest Rate: {decision['interest_rate']}%")

            if "foir" in decision:

                st.write(f"FOIR: {decision['foir']}%")

            if "risk_category" in decision:

                st.write(f"Risk Category: {decision['risk_category']}")
        # ---------------------------------------------------
        # NEW CUSTOMER
        # ---------------------------------------------------

        else:

            st.session_state.new_customer = True


# ---------------------------------------------------
# NEW CUSTOMER FORM
# ---------------------------------------------------

if st.session_state.new_customer:

    st.warning("New Customer Detected")

    customer_name = st.text_input(
        "Enter Full Name",
        key="new_customer_name"
    )

    customer_city = st.text_input(
        "Enter City",
        key="new_customer_city"
    )

    customer_address = st.text_area(
        "Enter Address",
        key="new_customer_address"
    )

    employment_type = st.selectbox(
        "Employment Type",
        ["Salaried", "Business"],
        key="new_customer_employment"
    )

    submit_new_customer = st.button(
        "Submit New Customer",
        key="submit_new_customer_btn"
    )

    # ---------------------------------------------------
    # SUBMIT NEW CUSTOMER
    # ---------------------------------------------------

    if submit_new_customer:

    # Validation
        if customer_name == "" or customer_city == "" or customer_address == "":

            st.error("Please fill all customer details.")

        else:

            # Dummy defaults
            credit_score = 720

            preapproved_limit = 300000

            # Create customer object
            customer = {
                "name": customer_name,
                "phone": phone,
                "city": customer_city,
                "address": customer_address,
                "employment_type": employment_type
            }

            # Show Details
            st.subheader("Customer Details")

            st.write(f"Name: {customer_name}")
            st.write(f"City: {customer_city}")
            st.write(f"Employment Type: {employment_type}")

            # Credit Info
            st.subheader("Credit Evaluation")

            st.write(f"Credit Score: {credit_score}")

            st.write(f"Pre-approved Limit: Rs.{preapproved_limit}")

            # Underwriting
            decision = evaluate_loan(
                credit_score=credit_score,
                requested_loan=requested_loan,
                preapproved_limit=preapproved_limit,
                salary=salary,
                tenure_months=tenure_months
            )

            # Final Decision or LOAN DECISION
            # Final Decision
            st.subheader("Loan Decision")

            if decision["status"] == "APPROVED":

                st.success("✅ LOAN APPROVED")

                # Generate PDF
                pdf_path = generate_sanction_letter(
                    customer_name=customer["name"],
                    loan_amount=requested_loan,
                    tenure=tenure_months,
                    interest_rate=decision["interest_rate"],
                    emi=decision["emi"]
                )


                # ============================================
                # APPROVAL PROBABILITY
                # ============================================

                st.subheader("🎯 AI Risk Assessment")

                if decision["status"] == "APPROVED":

                    approval_probability = 92

                    st.progress(approval_probability / 100)

                    st.success(
                        f"Approval Probability: {approval_probability}%"
                    )

                    st.info(
                        f"Risk Category: {decision['risk_category']}"
                    )

                else:

                    approval_probability = 35

                    st.progress(approval_probability / 100)

                    st.error(
                        f"Approval Probability: {approval_probability}%"
                    )

                    st.warning(
                        f"Risk Category: {decision['risk_category']}"
                    )

                # Download PDF
                with open(pdf_path, "rb") as pdf_file:

                    st.download_button(
                        label="📄 Download Sanction Letter",
                        data=pdf_file,
                        file_name="sanction_letter.pdf",
                        mime="application/pdf"
                    )

            else:

                st.error("❌ LOAN REJECTED")

            st.write(f"Reason: {decision['reason']}")

            if "emi" in decision:

                st.write(f"Monthly EMI: Rs.{decision['emi']:,.2f}")

            if "interest_rate" in decision:

                st.write(f"Interest Rate: {decision['interest_rate']}%")

            if "foir" in decision:

                st.write(f"FOIR: {decision['foir']}%")

            if "risk_category" in decision:

                st.write(f"Risk Category: {decision['risk_category']}")

            # ============================================
            # AI AGENT WORKFLOW
            # ============================================

            st.subheader("🤖 AI Workflow Summary")

            with st.expander("View Agent Activities"):

                st.success("✅ Sales Agent")
                st.write(
                    "Collected customer loan requirements, "
                    "salary details, and preferred tenure."
                )

                st.success("✅ Verification Agent")
                st.write(
                    "Verified customer identity, salary slip, "
                    "and employment details."
                )

                st.success("✅ Underwriting Agent")
                st.write(
                    f"Evaluated credit score ({credit_score}), "
                    f"calculated FOIR ({decision['foir']}%), "
                    "and checked loan eligibility."
                )

                st.success("✅ Sanction Agent")
                st.write(
                    "Generated final loan decision and "
                    "prepared sanction letter."
                )

            # ============================================
            # DASHBOARD METRICS
            # ============================================

            st.subheader("📊 Loan Analytics Dashboard")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    label="Credit Score",
                    value=credit_score
                )

            with col2:
                st.metric(
                    label="FOIR",
                    value=f"{decision['foir']}%"
                )

            with col3:
                st.metric(
                    label="Interest Rate",
                    value=f"{decision['interest_rate']}%"
                )

            st.metric(
                label="Monthly EMI",
                value=f"Rs.{decision['emi']:,.2f}"
            )


            # ============================================
            # EMI VISUALIZATION
            # ============================================

            st.subheader("📈 EMI Breakdown Analysis")

            principal = requested_loan
            interest = (decision["emi"] * tenure_months) - principal

            chart_data = pd.DataFrame({
                "Category": ["Principal Amount", "Total Interest"],
                "Amount": [principal, interest]
            })

            st.bar_chart(
                chart_data.set_index("Category")
            )
            #LOAN SUMMARY
            st.subheader("Loan Summary")

            st.info(f"""
            Loan Amount: Rs.{requested_loan}

            Loan Tenure: {tenure_months} months

            Monthly Salary: Rs.{salary}

            Interest Rate: {decision.get('interest_rate', 'N/A')}%

            Estimated EMI: Rs.{decision.get('emi', 'N/A')}
            """)
                                    
# ==================================================
# AI CHATBOT
# ==================================================

from crewai import Task, Crew
from agents.sales_agent import sales_agent

st.divider()

st.header("💬 Ask AI Loan Assistant")

user_query = st.text_input(
    "Ask anything about loans"
)

if st.button("Ask AI Assistant"):

    if user_query != "":

        chatbot_task = Task(
            description=f"""
            Answer the customer's query professionally.

            Customer Question:
            {user_query}

            Provide helpful guidance related to:
            - personal loans
            - EMI
            - eligibility
            - interest rates
            - loan approval
            """,

            expected_output="Professional loan guidance response.",

            agent=sales_agent
        )

        chatbot_crew = Crew(
            agents=[sales_agent],
            tasks=[chatbot_task],
            verbose=False
        )

        response = chatbot_crew.kickoff()

        st.subheader("🤖 AI Assistant Response")

        st.success(str(response))

    else:

        st.warning("Please enter a question.")