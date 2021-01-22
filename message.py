
import smtplib

EMAIL_ADDRESS = 'dinglechas@gmail.com'
EMAIL_PASSWORD = 'gH0st567'

#sets up a port 587 in this case is needed or otherwise the SMTP server will shut down
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
#logs into your email in the SMTP
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#sets vars for the content of the email
    subject = 'grab dinner this weekend'
    body = 'how about dinner at 6pm this saturday?'
#add the vars
    msg = f'subject: {subject}\n\n{body}'

#sends the email
    smtp.sendmail(EMAIL_ADDRESS, 'chasdingl3@gmail.com', msg)