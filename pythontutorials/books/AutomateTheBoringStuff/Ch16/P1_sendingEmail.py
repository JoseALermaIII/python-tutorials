"""Sending email

This program uses :py:mod:`smtplib` to send emails.

Notes:
    * ``smtp_info`` file has each item on a separate line.
    * Email address used is specially created for this chapter.
    * Use :func:`input` for password to prevent storing in unencrypted file.

"""


def main():
    # Connecting to an SMTP Server
    import smtplib

    with open('smtp_info') as config:
        email, password, server, port = config.read().splitlines()

    smtp_obj = smtplib.SMTP_SSL(server, port)  # Using port 465
    print(type(smtp_obj))

    # Sending the SMTP "Hello" Message
    print(smtp_obj.ehlo())

    # Logging in to the SMTP Server
    print(smtp_obj.login(email, password))

    # Sending an Email
    unsent = smtp_obj.sendmail(email, 'contact.me@JoseALerma.com',
                               'Subject: Bot test.\nDear Myself,\nAlways remember that with great '
                               'power comes great responsibility.\nRegards,\nYou')
    print(unsent.keys())

    # Disconnecting from the SMTP Server
    print(smtp_obj.quit())


if __name__ == '__main__':
    main()
