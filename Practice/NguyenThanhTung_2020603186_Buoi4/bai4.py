import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    sender_email = "0975759485as@gmail.com"
    sender_password = "xaqgwnihpmetjsxt"

    receiver_emails = [
        "test1@gmail.com",
        "test1@haui.edu.vn",
        "test1@icloud.com",
        "test1@outlook.com"
    ]
    subject = "Subject of the Email"
    body = "Body of the Email"

    try:
        for receiver_email in receiver_emails:
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject

            message.attach(MIMEText(body, "plain"))

            smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.login(sender_email, sender_password)
            smtp_server.sendmail(sender_email, receiver_email, message.as_string())
            smtp_server.quit()

            print(f"Đã gửi email thành công tới: {receiver_email}")

    except smtplib.SMTPException as e:
        print("Đã xảy ra lỗi khi gửi email:", str(e))

send_email()
