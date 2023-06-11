# This code was developed by Nguyen Van Cuong
# Thank you so much for reading and looking into my code

import smtplib
from email.message import EmailMessage

EMAIL = 'laptrinhmang@outlook.com'
PASSWORD = 'LTM.DHCNHN.HaUI'
DESTINATION_EMAIL = 'laptrinhmang.haui@gmail.com'

SUBJECT_EMAIL = "Tiêu đề: Lập trình mạng"
BODY_EMAIL = "Thân gửi An,\n\nNội dung thư điện tử.\n\nTrân trọng."

msg = EmailMessage()
msg['To'] = DESTINATION_EMAIL
msg['From'] = EMAIL
msg['Subject'] = SUBJECT_EMAIL
msg.set_content(BODY_EMAIL)

mailServer = 'smtp.office365.com'
mailPort = 587

connection = smtplib.SMTP(mailServer, mailPort)
connection.starttls()
connection.login(EMAIL, PASSWORD)
connection.send_message(msg=msg, from_addr=EMAIL, to_addrs=DESTINATION_EMAIL)
connection.quit()
