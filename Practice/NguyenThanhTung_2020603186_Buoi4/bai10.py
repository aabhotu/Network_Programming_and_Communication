import imaplib
import email

def fetch_email_details(message_number):
    username = "0975759485as@gmail.com"
    password = "xaqgwnihpmetjsxt"
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(username, password)
        mail.select("INBOX")
        status, response = mail.fetch(str(message_number), "(RFC822)")
        raw_email = response[0][1]
        email_message = email.message_from_bytes(raw_email)
        sender = email_message["From"]
        recipient = email_message["To"]
        subject = email_message["Subject"]
        content = ""
        if email_message.is_multipart():
            for part in email_message.walk():
                content_type = part.get_content_type()
                if content_type == "text/plain" or content_type == "text/html":
                    content = part.get_payload(decode=True).decode()
                    break
        else:
            content_type = email_message.get_content_type()
            if content_type == "text/plain" or content_type == "text/html":
                content = email_message.get_payload(decode=True).decode()
        print("----- Tin nhắn -----")
        print("Gửi từ:", sender)
        print("Nhận bởi:", recipient)
        print("Tiêu đề:", subject)
        print("Nội dung:")
        print(content)
        print("--------------------")
        print()
        mail.logout()

    except imaplib.IMAP4.error as e:
        print("Đã xảy ra lỗi khi truy cập hòm thư:", str(e))

fetch_email_details(1)
