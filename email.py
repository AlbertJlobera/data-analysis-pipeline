import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
import csv
import yagmail


def Email():
    subject='Nintendo sales'
    body= """  
    Hello,

    As you ordered, we finished the project about all sales from 1980 until 2000, you have two parametres to check the data. We clean all 
    dataset so, be free to check the decada and country, the program will show you exactly the sum of that.
    Remember to us the parametres as I said or you cann check it with --help in terminal.
    I've attached a PDF with the a brief summary of the information, with a graphic.
    For anything else fell free to pop up to my office.

    Regards,
    Albert Jose Lobera
    Data Analyst in Nintendo
    tlf: 682.63.35.67 ext: 1232
    """
    sender_email = input('Sender email: ')
    receiver_email = input('Destinatary_email: ')
    password=input('Password: ')

    message=MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message.attach(MIMEText(body, 'plain'))
    filename = 'Nintendo_Sales_pdf'
    with open(filename,'rb') as attachment:
        part = MIMEBase('application','octet-stream')
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        'Content-Disposition',
        f'attachment;filename={filename}',
    )
    message.attach(part)
    text = message.as_string()

    context= ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as server:
        server.login(sender_email,pasword)
        server.sendmail(sender_email,receiver_email, text)