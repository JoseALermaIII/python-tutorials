#! python3
# P05_textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string.

from twilio.rest import TwilioRestClient

# Preset values:
with open('twilio_info') as config:
    accountSID, authToken, twilioNumber, myNumber = config.read().splitlines()


def textmyself(message):
    twilioCli = TwilioRestClient(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
    return None
