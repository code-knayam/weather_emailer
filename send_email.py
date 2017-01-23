import smtplib


def send_emails(emails, forecast):
    # connect to smtp server
    server = smtplib.SMTP('smtp.gmail.com','587')

    #start TLS encryption
    server.starttls()

    #prompting login ID
    from_email = input('Enter login id - ')
    #prompting for password
    password = input("Enter password - ")
    #Log In
    server.login(from_email, password)

    #send to entire email list
    for to_email, name in emails.items():
        message = 'Subject: Weather App Forecast\n'
        message += ' Hi, ' + name + '!\n\n'
        message += forecast + '\n\n'
        message += 'Thanks, \n Mayank Jain'
        server.sendmail(from_email, to_email, message)

    #quitting server
    server.quit()
