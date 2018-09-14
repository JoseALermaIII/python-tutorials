# This program uses the smtplib module to send emails

# Connecting to an SMTP Server
import smtplib

with open('smtp_info') as config:
    # smtp_cfg = [email, password, smtp server, port]
    smtp_cfg = config.read().splitlines()

smtp_obj = smtplib.SMTP_SSL(smtp_cfg[2], smtp_cfg[3])
print(type(smtp_obj))
