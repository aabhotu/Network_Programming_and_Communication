
import dns.resolver
def lookup(hostname, qtype):
  answer = dns.resolver.resolve(hostname, qtype, raise_on_no_answer=False)
  if answer.rrset is not None:
    print(f"ban ghi loai {qtype} cua host name {hostname}: {answer.rrset[0]}")
  else:
    print("khong tim thay")

hostnames = ['fee.haui.edu.vn', 'python.org']
qtypes = ['A', 'AAAA', 'CNAME', 'MX', 'NS']
for hostname in hostnames:
  print(hostname)
  for qtype in qtypes:
    lookup(hostname, qtype)