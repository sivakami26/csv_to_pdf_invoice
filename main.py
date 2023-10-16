import pathlib

import pandas as pd
import glob
from fpdf import FPDF

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = pathlib.Path(filepath).stem
    invoice_nr = filename.split("-")[0]
    date = filename.split("-")[1]
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)
    pdf.set_font(family="Times", size=8, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    columns = [item.replace("_", " ").title() for item in df.columns]
    pdf.set_font(family="Times", size=8, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=70, h=8, txt=columns[1], border=1)
    pdf.cell(w=30, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    for index, rows in df.iterrows():
        pdf.set_font(family="Times", size=8)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(rows["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=str(rows["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(rows["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(rows["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(rows["total_price"]), border=1, ln=1)

    total_sum = df["total_price"].sum()
    pdf.set_font(family="Times", size=8)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=70, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=40, h=8, txt=f"The total price is {total_sum}", border=0, ln=1)

    pdf.set_font(family="Times", size=20)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=40, h=8, txt="PythonHow", border=0)
    pdf.image("pythonhow.png", w=10)
    pdf.output(f"PDFs/output_{invoice_nr}.pdf")
