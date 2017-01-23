import get_forecast
import send_email

def get_emails():
    emails = {}

    #getting mail list from txt file
    try:
        email_file = open('emails.txt', 'r')

        for email in email_file :
            (email, name ) = email.split(',')
            emails[email] = name.strip()
    except FileNotFoundError as err:
        print(err)

    return emails

def main():
    #calling required functions
    emails = get_emails()
    forecast = get_forecast.get_weather_forecast()
    send_email.send_emails(emails, forecast)

main()
