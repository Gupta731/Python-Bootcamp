This program sends an email to user whenever the international space station goes above their city after sunset, so that they can have a view of it.
I have made use of API requests for getting the current location of ISS and also the sunset and sunrise times at a specific latitude and longitude. I also had to work with timezone to convert the utc time into local time.
Concepts used: requests, os, smtplib, datetime and dateutil modules, environment variables, error handling, etc
