"""Send SMS

This program uses `twilio`_ to send SMS messages to a phone number.

Note:
    * ``twilio_info`` file has each item on a separate line.
    * Use :func:`input` to prevent storing sensitive info in unencrypted file.

.. _twilio:
    https://www.twilio.com/docs/sms

"""


def main():
    # Sending Text Messages
    from twilio.rest import Client

    with open('twilio_info') as config:
        accountSID, authToken, myTwilioNumber, myCellPhone = config.read().splitlines()

    twilioCli = Client(accountSID, authToken)
    message = twilioCli.messages.create(body='Mr. Watson - Come here - I want to see you.',
                                        from_=myTwilioNumber, to=myCellPhone)

    print(message.to)
    print(message.from_)
    print(message.body)
    print(message.status)
    print(message.date_created)
    print(message.date_sent is None)

    print(message.sid)
    updatedMessage = twilioCli.messages(message.sid).fetch()
    print(updatedMessage.status)
    print(updatedMessage.date_sent)


if __name__ == '__main__':
    main()
