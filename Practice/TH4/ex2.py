import poplib, imapclient

email = 'laptrinhmang@outlook.com'
password = 'LTM.DHCNHN.HaUI'
mailServer = 'outlook.office365.com'
popObj = poplib.POP3_SSL(mailServer)
imaObj = imapclient.IMAPClient(mailServer, ssl=True)
try:
  popObj.user(email)
  popObj.pass_(password)
  imaObj.login(email, password)
except:
  print("Login's not success")
else:
  respon, listings, octet_count = popObj.list()
  if not listings:
    print("k co")
  for listing in listings:
    number, size = listing.decode().split()
    print(f"Hom thu thu {number} co kich thuoc {size} bytes")
    pass
  print()
  data = imaObj.list_folders()
  for flags, delimiter, folder_name in data:
    print(flags[0].decode(), delimiter.decode(), folder_name)
    pass
finally:
  popObj.quit()
  imaObj.logout()