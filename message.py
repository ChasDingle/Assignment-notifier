
import smtplib

EMAIL_ADDRESS = 'email here'
EMAIL_PASSWORD = 'password here'

#sets up a port 587 in this case is needed or otherwise the SMTP server will shut down
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
#logs into your email in the SMTP
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#sets vars for the content of the email
    subject = 'subject here'
    body = 'body here'
#add the vars
    msg = f'subject: {subject}\n\n{body}'

#sends the email
    smtp.sendmail(EMAIL_ADDRESS, 'RECIEVER_ADDRESS', msg)
