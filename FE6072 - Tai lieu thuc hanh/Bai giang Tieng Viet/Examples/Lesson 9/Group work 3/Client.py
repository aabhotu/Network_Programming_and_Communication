# This code was developed by Nguyen Van Cuong
# Thank you so much for reading and looking into my code

import poplib, imapclient
EMAIL = 'laptrinhmang@outlook.com'
PASSWORD = 'LTM.DHCNHN.HaUI'
mailServer = 'outlook.office365.com'
POP_object = poplib.POP3_SSL(mailServer)
IMAP_object = imapclient.IMAPClient(mailServer, ssl=True,)
try:
  POP_object.user(EMAIL)
  POP_object.pass_(PASSWORD)
  IMAP_object.login(EMAIL, PASSWORD)
except:
  print("Đăng nhập không thành công")
else:
  response, listings, octet_count = POP_object.list()
  if not listings:
    print("Không có hòm thư nào")
  for listing in listings:
    number, size = listing.decode().split()
    print(f"Hòm thư thứ {number} có kích thước {size} bytes")
    pass
  print()
  data = IMAP_object.list_folders()
  for flags, delimiter, folder_name in data:
    print(flags[0].decode(), delimiter.decode(), folder_name)
    pass
finally:
  POP_object.quit()
  IMAP_object.logout()
