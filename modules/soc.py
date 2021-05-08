import socks

s = socks.socksocket() # Same API as socket.socket in the standard lib

s.set_proxy(socks.SOCKS5, "localhost") # SOCKS4 and SOCKS5 use port 1080 by default
# Or
s.set_proxy(socks.SOCKS4, "localhost", 4444)
# Or
s.set_proxy(socks.HTTP, "localhost", 8888)

# Can be treated identical to a regular socket object
s.connect(("www.python.org", 443))
s.sendall("GET / HTTP/1.1 ...")
print (s.recv(4096))