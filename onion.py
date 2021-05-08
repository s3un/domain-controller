import requests
import subprocess as subp

session = requests.session()
session.proxies = {}

session.proxies = {
    'http' : 'socks5h://localhost:80',
    'https' : 'socks5h://localhost:80'
}

response = session.get('http://httpbin.org/ip')
print(response.text)


# response = requests.get('http://httpbin.org/ip')
# print(response.text)