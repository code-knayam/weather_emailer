# weather_emailer
Sending current weather forecast to a mail list

Requires -
  Python 3
  request module (run - pip install requests - to install requests module )

Makes use of SMTP protocol to send emails.
When using gmail to send emails remember to Turn On Allow less secure apps Setting in Google account.
To do this -
  visit - https://myaccount.google.com
  then - Sign in & security
  search for - Allow less Secure apps
  Turn it on.

Add the Open Weather URL along with API key and location in get_forecast.py file.

Update the emails.txt file with emails and names of the users to be included.
