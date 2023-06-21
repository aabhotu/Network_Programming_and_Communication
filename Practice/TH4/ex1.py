import smtplib
from email.message import EmailMessage

email = 'laptrinhmang@outlook.com'
password = 'LTM.DHCNHN.HaUI'
des = 'laptrinhmang.haui@gmail.com'

subj = 'Tiêu đề: Lập trình mạng by tht'
body = "Thân gửi bạn An,\n\nNội dung thư điện tử.\n\nTrân trọng."

msg = EmailMessage()
msg['To'] = des
msg['From'] = email
msg['Subject'] = subj
msg.set_content(body)

mailServer = 'smtp.office365.com'
mailPort = 587

connection = smtplib.SMTP(mailServer, mailPort)
connection.starttls()
connection.login(email, password)
connection.send_message(msg=msg, from_addr=email, to_addrs=des)
connection.quit()