import imaplib

def get_message_sizes():
    username = "0975759485as@gmail.com"
    password = "xaqgwnihpmetjsxt"

    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")

        mail.login(username, password)

        mail.select("INBOX")

        status, response = mail.search(None, "ALL")
        message_ids = response[0].split()
        for message_id in message_ids:
            status, response = mail.fetch(message_id, "(RFC822.SIZE)")
            size = response[0].split()[2]
            print(f"Tin nhắn {message_id}: {size} bytes")

        mail.logout()

    except imaplib.IMAP4.error as e:
        print("Đã xảy ra lỗi khi truy cập hòm thư:", str(e))

get_message_sizes()
