from fpdf import FPDF
import webbrowser as wb
from IPython.display import Image
import pandas as pd
from path import *
# img=Image('../../Ironhack.png', 10, 8, 33)

pdf = FPDF ('P','mm','A4')
pdf.add_page()

pdf.set_font('Arial','B',20)

pdf.set_text_color(153,15,103)
pdf.text(95,25,'NINTENDO')

pdf.set_text_color(0)
# fpdf.cell(w, h = 0, txt = '', border = 0, ln = 0, 
# align = '', fill = False, link = '')
pdf.set_line_width(0)
pdf.set_font('Courier','B',12)

pdf.cell(30,60,'Decade',0,0,'C')

pdf.cell(40,60,'Europe Sales',0,0,'C')
pdf.cell(50,60,'North America Sales',0,0,'C')
pdf.cell(40,60,'Japan Sales',0,0,'C')
pdf.cell(30,60,'Global Sales',0,0,'C')
 #Global sales
pdf.set_font('Arial','',11)
pdf.set_text_color(199, 80, 82)
pdf.cell(-30,85,'237,86 milions',0,0,'C')
pdf.cell(33,120,'31,37 milions',0,0,'C')
pdf.cell(-34,155,'98,81 milions',0,0,'C')

#JP sales

pdf.cell(-40,85,'24,97%',0,0,'C')
pdf.cell(40,120,'11,27%',0,0,'C')
pdf.cell(-40,155,'11,31%',0,0,'C')

# NA sales

pdf.cell(-38,85,'112,33%',0,0,'C')
pdf.cell(38,120,'10,22%',0,0,'C')
pdf.cell(-38,155,'79,21%',0,0,'C')

# EU sales

pdf.cell(-55,85,'77,91%',0,0,'C')
pdf.cell(55,120,'8,89%',0,0,'C')
pdf.cell(-55,155,'6,49%',0,0,'C')

# Decade

pdf.cell(-30,85,'2000',0,0,'C')
pdf.cell(30,120,'1990',0,0,'C')
pdf.cell(-30,155,'1980',0,0,'C')

pdf.set_draw_color(199,80,131)
pdf.rect(10,45,190,1,'DF')

pdf.rect(10,100,190,1,'DF')

# images
pdf.image('ironhack.png', x=10, y= 5, w=20,h=20)

pdf.image('graphic nintendo.png', x=60, y= 130, w=100,h=100)

pdf.image('nintendo_logo.png', x=85, y= 240, w=60,h=20)

pdf.output('Nintendo_Sales_pdf','F')