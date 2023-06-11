# This code was developed by Nguyen Van Cuong
# Thank you so much for reading and looking into my code

import ftplib, os

host = 'ftp.ibiblio.org'

ftp = ftplib.FTP(host)
print("Welcome:", ftp.getwelcome())
ftp.login()

print(f"Đường dẫn hiện tại: {ftp.pwd()}")
ftp.cwd('/pub/linux/kernel')
print(f"Đường dẫn sau khi đổi: {ftp.pwd()}")
ftp.quit()