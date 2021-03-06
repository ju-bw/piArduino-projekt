#!/usr/bin/python3
import picamera, smtplib, sys
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

frm  = 'Michael Kofler <kofler@kofler.info>'
to   = 'Michael Kofler <michael.kofler@gmx.com>'
subj = 'Test-Mail von Python mit äöüß'
txt  = 'Das ist\nder Nachrichtentext mit äöüß.'
fn   = 'foto.jpg'  # diese Bitmap-Datei mitsenden

try:
  # Foto erstellen
  camera = picamera.PiCamera()
  camera.capture(fn, resize=(640,480))
  camera.close()

  # E-Mail zusammensetzen
  mime = MIMEMultipart()
  mime['From'] = frm
  mime['To']   = to
  mime['Subject'] = Header(subj, 'utf-8')
  mime.attach(MIMEText(txt, 'plain', 'utf-8'))

  # Bild hinzufügen
  f = open(fn, 'rb')
  img = MIMEImage( f.read() )
  f.close()
  mime.attach(img)

  # versenden
  smtp = smtplib.SMTP("kofler.info")
  smtp.starttls()
  smtp.login("kofler", "xxx")
  smtp.sendmail(frm, [to], mime.as_string())
  smtp.quit()
except:
  print("Beim E-Mail-Versand ist ein Fehler aufgetreten:", sys.exc_info())
  