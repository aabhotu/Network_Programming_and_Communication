# This code was developed by Nguyen Van Cuong
# Thank you so much for reading and looking into my code

import smtplib
from email.message import EmailMessage

EMAIL = 'laptrinhmang@outlook.com'
PASSWORD = 'LTM.DHCNHN.HaUI'
DESTINATION_EMAIL = ['laptrinhmang.haui@outlook.com', 'laptrinhmang.haui@gmail.com']

SUBJECT_EMAIL = "Title: Network programming"
BODY_EMAIL = "Dear Professor,\n\nExample for introducing Network programming course. " \
             "I has sent you research report as in the attached files.\n\nSincerely."

msg = EmailMessage()
msg['To'] = DESTINATION_EMAIL
msg['From'] = EMAIL
msg['Subject'] = SUBJECT_EMAIL
msg.set_content(BODY_EMAIL)

attachment_paths = ['content.txt','content.rar',]
for attachment_path in attachment_paths:
  filetype = attachment_path.split('.')[1]
  with open(attachment_path, 'rb') as f:
    data = f.read()
  msg.add_attachment(data, maintype='text', subtype='plain', filename=f.name)
  pass

mailServer = 'smtp.office365.com'
mailPort = 587

connection = smtplib.SMTP(mailServer, mailPort)
connection.starttls()
connection.login(EMAIL, PASSWORD)
connection.send_message(msg=msg, from_addr=EMAIL, to_addrs=DESTINATION_EMAIL)
connection.quit()