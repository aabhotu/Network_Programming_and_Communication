import dns.resolver

def lookup(hostname):
 # Đây là hàm dùng để truy vấn thông tin DNS cho một hostname cụ thể.
 qtype = 'A'#Gán giá trị 'A' cho biến qtype. Trong trường hợp này, chúng ta muốn truy vấn địa chỉ IPv4 (bản ghi A).
 answer = dns.resolver.resolve(hostname, qtype, raise_on_no_answer=False)
 # Sử dụng hàm resolve() của dns.resolver để truy vấn thông tin IPv4 (bản ghi A) cho hostname được cung cấp.
 # Tham số qtype chỉ định loại bản ghi cần truy vấn. raise_on_no_answer=False được sử dụng để tránh lỗi nếu không tìm thấy câu trả lời.
 if answer.rrset is not None:
  #Kiểm tra xem có câu trả lời từ truy vấn A hay không.
  print(f"Loại bản ghi: {qtype}")
  #In ra loại bản ghi đang được truy vấn, trong trường hợp này là A.
  print(f"Thời gian tồn tại của bản ghi: {answer.rrset.ttl}")
  # In ra thời gian tồn tại của bản ghi (Time to Live - TTL). answer.rrset.ttl truy cập vào thuộc tính ttl của câu trả lời để lấy giá trị TTL.
  print(f"Địa chỉ IPv4:")
  # In ra thông báo "Địa chỉ IPv4:
  for item in answer.rrset.items:
   # Lặp qua tất cả các địa chỉ IPv4 được trả về bởi truy vấn.
    print(" ",item)# In ra mỗi địa chỉ IPv4 trên một dòng riêng.
  pass#Đảm bảo không có lỗi cú pháp trong hàm lookup().
hostname = 'dhcnhn.vn'#Gán giá trị 'dhcnhn.vn' cho biến hostname.
print(f"Hostname: {hostname}")
# In ra thông báo "Hostname:" cùng với giá trị của hostname.
lookup(hostname)
# Gọi hàm lookup() với hostname là 'dhcnhn.vn' và in ra k