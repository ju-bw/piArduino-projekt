#!/usr/bin/python3
import smtplib, sys
from email.mime.text import MIMEText
from email.header import Header

frm  = 'Michael Kofler <kofler@kofler.info>'
to   = 'Michael Kofler <bugs@kofler.info>'
subj = 'Test-Mail von Python mit äöüß'
msg  = 'Das ist\nder Nachrichtentext mit äöüß.'

try:
  mime = MIMEText(msg, 'plain', 'utf-8')
  mime['From'] = frm
  mime['To']   = to
  mime['Subject'] = Header(subj, 'utf-8')

  smtp = smtplib.SMTP("kofler.info")
  smtp.starttls()
  smtp.login("kofler", "xxx")
  smtp.sendmail(frm, to, mime.as_string())
  smtp.quit()
except:
  print("Beim E-Mail-Versand ist ein Fehler aufgetreten:", sys.exc_info())