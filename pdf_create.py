from fpdf import FPDF
import webbrowser as wb
from IPython.display import Image
import pandas as pd
from path import *
# img=Image('../../Ironhack.png', 10, 8, 33)
def pdf_create():
    
    pdf=FPDF('P','mm','A4')
    pdf.add_page()
    pdf.set_font('Arial','B',14)
    pdf.cell(0,10,'NINTENDO',1,1,'C')
    pdf.output('report.pdf')
    return wb.open_new('report.pdf')

df = pd.DataFrame(df)
pdf_create()