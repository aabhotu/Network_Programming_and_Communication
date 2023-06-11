# This code was developed by Nguyen Van Cuong
# Thank you so much for reading and looking into my code

import dns.resolver

def lookup(hostname):
  qtypes = ['NS', 'MX']
  for qtype in qtypes:
    answer = dns.resolver.resolve(hostname, qtype, raise_on_no_answer=False)
    if answer.rrset is not None:
      print(f"Loại bản ghi: {qtype}")
      print(f"Thời gian tồn tại của bản ghi: {answer.rrset.ttl}")
      if qtype=='NS':
        print(f"Tên chính tắc của tên miền: {hostname}")
      elif qtype=='MX':
        print(f"Tên của máy chủ thư điện tử được liên kết với tên miền: {hostname}")
      for item in answer.rrset.items:
        print(" ",item)
  pass

hostname = 'outlook.com'
print(f"Hostname: {hostname}")
lookup(hostname)