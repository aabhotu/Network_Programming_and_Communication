# This code was developed by Nguyen Van Cuong
# Thank you so much for reading and looking into my code

import ftplib, os

host = '192.168.1.164'
filename = 'ABC.txt'

ftp = ftplib.FTP(host)
print("Welcome:", ftp.getwelcome())
ftp.login()

print(f"Đường dẫn hiện tại: {ftp.pwd()}")
ftp.cwd('/New folder')
print(f"Đường dẫn sau khi đổi: {ftp.pwd()}")

if os.path.exists(filename):
  print(f"Ghi đè tập tin {filename}")

with open(filename, 'wb') as f:
  ftp.retrbinary(f"RETR {filename}", f.write)
  pass

ftp.quit()