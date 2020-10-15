#!/usr/bin/env python2
'''
Send Email via SMTP
ingat enable less secure app
'''
import smtplib
import getpass
from email.mime.text import MIMEText

SERVER = 'smtp-mail.outlook.com'
PORT = 587
SENDER = 'email'
RECEIVER = 'email'
SUBJ = 'Tugas Network Programming kelas XX151'
DATE = '25 May 2028 18:00:00 +0800'
MSG = MIMEText('SCRIPT | 150010310')

MSG['Subject'] = SUBJ
MSG['From'] = SENDER
MSG['To'] = RECEIVER
MSG['Date'] = DATE

try:
    S = smtplib.SMTP(SERVER,PORT)
    S.starttls()
    #S.ehlo()
    S.ehlo_or_helo_if_needed()
    S.login(SENDER, getpass.getpass())
    S.sendmail(SENDER, [RECEIVER], MSG.as_string())
    S.close()
    print 'Pesan terkirim'
except smtplib.SMTPException as smtpe:
    print smtpe.message
