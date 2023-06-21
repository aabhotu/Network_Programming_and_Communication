# import dns.resolver
#
# def lookup(hostname, qtype):
#   answer = dns.resolver.resolve(hostname, qtype, raise_on_no_answer=False)
#   for item in answer.rrset.items:
#     item = str(item.target)[0:len(str(item.target)) - 1]
#     answer1 = dns.resolver.resolve(item, "A", raise_on_no_answer=False)
#     print(answer1[0])
#
# hostname = "gmail.com"
# qtype = "NS"
# print("IP cua cac may chu duoc uy quyen: ")
# lookup(hostname, qtype)

import dns.resolver

def lookup(hostname, qtype):
  answer = dns.resolver.resolve(hostname, qtype, raise_on_no_answer=False)
  for i in answer.rrset.items:
    i = str(i.target)[0:len(str(i.target))-1]
    # print(i)
    answer1 = dns .resolver.resolve(i, 'A', raise_on_no_answer=False)
    print(answer1[0])
hostname = 'gmail.com'
qtype = 'NS'
print("ip dc uy quyen: ")
lookup(hostname,qtype)