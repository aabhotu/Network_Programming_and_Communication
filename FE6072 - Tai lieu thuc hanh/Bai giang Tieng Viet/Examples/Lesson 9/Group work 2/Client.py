# This code was developed by Nguyen Van Cuong
# Thank you so much for reading and looking into my code

import smtplib
from email.message import EmailMessage

EMAIL = 'laptrinhmang@outlook.com'
PASSWORD = 'LTM.DHCNHN.HaUI'
DESTINATION_EMAIL = 'laptrinhmang.haui@gmail.com'

SUBJECT_EMAIL = "Báo cáo nhóm"
BODY_EMAIL = "Thân gửi An,\n\nTôi gửi bạn báo cáo được đính kèm trong email này.\n\nTrân trọng."

msg = EmailMessage()
msg['To'] = DESTINATION_EMAIL
msg['From'] = EMAIL
msg['Subject'] = SUBJECT_EMAIL
msg.set_content(BODY_EMAIL)

attachment_path = 'content.rar'
with open(attachment_path, 'rb') as f:
  data = f.read()
msg.add_attachment(data, maintype='text', subtype='plain', filename=f.name)

mailServer = 'smtp.office365.com'
mailPort = 587

connection = smtplib.SMTP(mailServer, mailPort)
connection.starttls()
connection.login(EMAIL, PASSWORD)
connection.send_message(msg=msg, from_addr=EMAIL, to_addrs=DESTINATION_EMAIL)
connection.quit()