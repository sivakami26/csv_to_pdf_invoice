import pathlib
import glob
from fpdf import FPDF

filepaths = glob.glob("Text_Files/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")
for filepath in filepaths:
    pdf.add_page()
    filename = pathlib.Path(filepath).stem
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"{filename.title()}", ln=1)

    with open(f"Text_files/{filename}.txt", 'r') as file:
        content = file.read()
    pdf.set_font(family="Times", size=10)
    pdf.multi_cell(w=0, h=8, txt=content)


pdf.output("output.pdf")
