import dns.resolver

def lookup(hostname):
  answer = dns.resolver.resolve(hostname, 'MX', raise_on_no_answer=False)
  if answer.rrset is not None:
    for ans in answer.rrset:
      email_server = ans.exchange.to_text(omit_final_dot=False)
      ipv6 = dns.resolver.resolve(email_server, 'AAAA', raise_on_no_answer=False)
      if ipv6 is not None:
        print(f"dia chi ipv6 tuong ung voi {email_server}: {ipv6.rrset[0]}")
      else:
        print("khong co dia chi ipv6")
  else:
    print("Khong co MCTDT")
hostname = 'python.org'
print(hostname)
lookup(hostname)