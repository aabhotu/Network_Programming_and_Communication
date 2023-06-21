import dns.resolver

def lookup(hostname):
  qtype = 'A'
  answer = dns.resolver.resolve(hostname, qtype, raise_on_no_answer=False)
  if answer.rrset is not None:
    print(f"Loai ban ghi: {qtype}")
    print(f"Thoi gian ton tai ban ghi: {answer.rrset.ttl}")
    print(f"Dia chi Ipv4: ")
    for i in answer.rrset.items:
      print(" ", i)
      pass
hostname = 'google.com'
print(f"Hostname: {hostname}")
lookup(hostname)