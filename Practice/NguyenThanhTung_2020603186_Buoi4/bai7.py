import poplib

def check_mailbox_status():
    username = "0975759485as@gmail.com"
    password = "xaqgwnihpmetjsxt"

    try:
        mail = poplib.POP3_SSL("pop.gmail.com")
        mail.user(username)
        mail.pass_(password)
        status = mail.stat()

        message_count = status[0]
        mailbox_size = status[1]

        print(f"Số tin nhắn: {message_count}")
        print(f"Kích thước hòm thư: {mailbox_size} bytes")

        mail.quit()

    except poplib.error_proto as e:
        print("Đã xảy ra lỗi khi truy cập hòm thư:", str(e))

check_mailbox_status()
