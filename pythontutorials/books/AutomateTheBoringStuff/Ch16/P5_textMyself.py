#! python3
"""P5_textMyself.py

Defines :func:`textmyself` that texts a string message passed to it.

Note:
    * ``twilio_info`` file has each item on a separate line.
    * Use :func:`input` to prevent storing sensitive info in unencrypted file.

"""

from twilio.rest import Client

# Preset values:
filepath = '/home/jose/PycharmProjects/python-tutorials/pythontutorials/books/AutomateTheBoringStuff/Ch16/twilio_info'
with open(filepath) as config:
    accountSID, authToken, twilioNumber, myNumber = config.read().splitlines()


def textmyself(message: str) -> None:
    """Text myself

    Sends given message as SMS to twilio account specified in ``./twilio_info``.

    Args:
        message: String containing message to be sent.

    Returns:
        None. Message is sent to twilio phone number.

    """
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
