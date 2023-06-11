# This code was developed by Nguyen Van Cuong
# Thank you so much for reading and looking into my code

import dns.resolver

def lookup(hostname):
  qtype = 'A'
  answer = dns.resolver.resolve(hostname, qtype, raise_on_no_answer=False)
  if answer.rrset is not None:
    print(f"Loại bản ghi: {qtype}")
    print(f"Thời gian tồn tại của bản ghi: {answer.rrset.ttl}")
    print(f"Địa chỉ IPv4:")
    for item in answer.rrset.items:
      print(" ",item)
  pass

hostname = 'dhcnhn.vn'
print(f"Hostname: {hostname}")
lookup(hostname)
