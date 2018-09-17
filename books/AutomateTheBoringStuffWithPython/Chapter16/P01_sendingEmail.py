# This program uses the smtplib module to send emails
#
# Note:
# - smtp_info file has each item on separate line
# - email address used is specially created for this chapter
# - use input() for password to prevent storing in unencrypted file

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
