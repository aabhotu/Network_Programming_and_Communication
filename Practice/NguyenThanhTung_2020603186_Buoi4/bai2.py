import imaplib

def analyze_mailbox():
    username = "0975759485as@gmail.com"
    password = "xaqgwnihpmetjsxt"

    try:
        mail_server = imaplib.IMAP4_SSL("imap.gmail.com")
        mail_server.login(username, password)
        response, mailbox_list = mail_server.list()

        if response == "OK":
            print("Các thư mục trong hòm thư:")
            for mailbox in mailbox_list:
                mailbox_name = mailbox.decode().split('"/"')[-1].strip('"')

                print(mailbox_name)

        mail_server.select("INBOX")

        response, message_list = mail_server.search(None, "ALL")

        if response == "OK":
            print("Kích thước của từng tin nhắn:")
            for message_id in message_list[0].split():
                response, message_data = mail_server.fetch(message_id, "(RFC822.SIZE)")

                if response == "OK":
                    message_size = message_data[0].decode().split()[-1]
                    print(f"Tin nhắn {message_id.decode()}: {message_size} bytes")

        mail_server.close()
        mail_server.logout()
    except imaplib.IMAP4.error as e:
        print("Đã xảy ra lỗi khi phân tích hòm thư:", str(e))

analyze_mailbox()
