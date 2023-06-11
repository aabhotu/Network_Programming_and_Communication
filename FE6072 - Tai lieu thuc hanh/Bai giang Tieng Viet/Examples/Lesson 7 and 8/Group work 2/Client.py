# This code was developed by Nguyen Van Cuong
# Thank you so much for reading and looking into my code

import dns.resolver

def lookup(hostname):
  qtype = 'NS'
  answer = dns.resolver.resolve(hostname, qtype, raise_on_no_answer=False)
  if answer.rrset is not None:
    print(f"Loại bản ghi: {qtype}")
    print(f"Thời gian tồn tại của bản ghi: {answer.rrset.ttl}")
    print(f"Tên máy chủ thẩm quyển cho tên miền: {hostname}")
    for item in answer.rrset.items:
      print(" ",item)
  pass

hostname = 'office365.com'
print(f"Hostname: {hostname}")
lookup(hostname)