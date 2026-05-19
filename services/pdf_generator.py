from fpdf import FPDF
from datetime import datetime


def generate_sanction_letter(
    customer_name,
    loan_amount,
    tenure,
    interest_rate,
    emi,
    output_path="sanction_letter.pdf"
):

    pdf = FPDF()

    pdf.add_page()

    # Title
    pdf.set_font("Arial", "B", 18)

    pdf.cell(
        200,
        10,
        txt="NBFC PERSONAL LOAN SANCTION LETTER",
        ln=True,
        align="C"
    )

    pdf.ln(15)

    # Date
    pdf.set_font("Arial", "", 12)

    current_date = datetime.now().strftime("%d-%m-%Y")

    pdf.cell(
        200,
        10,
        txt=f"Date: {current_date}",
        ln=True
    )

    pdf.ln(10)

    # Customer Greeting
    pdf.multi_cell(
        0,
        10,
        txt=f"""
Dear {customer_name},

Congratulations!

Your personal loan application has been approved.

Below are your loan details:
"""
    )

    pdf.ln(5)

    # Loan Details
    pdf.set_font("Arial", "B", 12)

    pdf.cell(80, 10, "Loan Amount:")
    pdf.cell(80, 10, f"Rs.{loan_amount:,.2f}", ln=True)

    pdf.cell(80, 10, "Loan Tenure:")
    pdf.cell(80, 10, f"{tenure} months", ln=True)

    pdf.cell(80, 10, "Interest Rate:")
    pdf.cell(80, 10, f"{interest_rate}%", ln=True)

    pdf.cell(80, 10, "Monthly EMI:")
    pdf.cell(80, 10, f"Rs.{emi:,.2f}", ln=True)

    pdf.ln(15)

    # Closing Message
    pdf.set_font("Arial", "", 12)

    pdf.multi_cell(
        0,
        10,
        txt="""
Thank you for choosing our financial services.

We look forward to serving you.

Regards,
NBFC Loan Department
"""
    )

    # Save PDF
    pdf.output(output_path)

    return output_path