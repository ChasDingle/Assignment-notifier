# A simple calculator example
# Based on example found in programminginpython.com
# Modified for instructional purposes
#imports a library so we have to write less code when writing our gui
import tkinter as tk

# Creates a window of a particular size and colour
root = tk.Tk()
root.title("Scrape Service")
root.geometry('400x200')
root.configure(bg='orange')

# Helper functions to support button action
#this is what we would have from the scraper
thislist = ('Crit A','Crit B','Crit C','Crit D',)







# Creating all of the labels with text information
labelTitle = tk.Label(root, text="Let's Scrape a Website!")
labelUrl = tk.Label(root, text="Enter Website URL")
labelEmail = tk.Label(root, text="Enter Email Address")
labelAns = tk.Label(root, text="The answer is")

# Arranging all of the labels in a "grid"
labelTitle.grid(row=0, column=2)
labelUrl.grid(row=1, column=0)
labelEmail.grid(row=2, column=0)
labelAns.grid(row=3, column=0)

# Here is where we take our inputs
entryUrl = tk.Entry(root,)

entryUrl.grid(row=1, column=2)

entryEmail = tk.Entry(root,)

entryEmail.grid(row=2, column=2)



def clicked():
    #imports the library that allows us to send emails
    import smtplib
    #gives address and password to login to send email
    EMAIL_ADDRESS = 'email here'
    EMAIL_PASSWORD = 'password here'

    # sets up a port 587 in this case is needed or otherwise the SMTP server will shut down
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
    # logs into your email in the SMTP
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    # sets vars for the content of the email
            subject = 'SUMMATIVE NOTIFIER'
            body = thislist[-1]
    # add the vars
            msg = f'subject: {subject}\n\n{body}'
           #gets the email address from the input box
            email = (entryEmail.get())
            #sends the email
            smtp.sendmail(EMAIL_ADDRESS, str(email), msg)
    #takes the last item from the list and puts it on the screen aswells as giving the confirmation email is sent
    result = thislist[-1]
    labelAns.config(text="Sent: " + (result))





#Here is where we set up the button to perform "call"
#Email is performed when the "clicked" function is called
buttonEmail = tk.Button(root, text="Notify", command=clicked)
buttonEmail.grid(row=5, column=0)

#Main Loop
root.mainloop()
