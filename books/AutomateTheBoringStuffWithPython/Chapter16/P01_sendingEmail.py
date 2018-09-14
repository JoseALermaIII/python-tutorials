# This program uses the smtplib module to send emails
#
# Note:
# - smtp_info file has each item on separate line
# - email address used is specially created for this chapter
# - use input() for password to prevent storing in unencrypted file

# Connecting to an SMTP Server
import smtplib

with open('smtp_info') as config:
    # smtp_cfg = [email, password, smtp server, port]
    smtp_cfg = config.read().splitlines()

smtp_obj = smtplib.SMTP_SSL(smtp_cfg[2], smtp_cfg[3])  # Using port 465
print(type(smtp_obj))

# Sending the SMTP "Hello" Message
print(smtp_obj.ehlo())

# Logging in to the SMTP Server
print(smtp_obj.login(smtp_cfg[0], smtp_cfg[1]))
