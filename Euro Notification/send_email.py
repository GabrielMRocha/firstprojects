from email.mime.text import MIMEText
import smtplib

def send_email(email, cotacao):
    from_email="gabca.robo@gmail.com"
    from_password="R0b0.Gabca"
    to_email=email

    subject="Cotação do Euro"
    message="Oi mãe! A cotação o euro hoje é %s  " % (cotacao)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
