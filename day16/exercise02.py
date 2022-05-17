# author:xiao kun time:5/12/22
from select import *
from socket import *
import time

udp_sock = socket(AF_INET, SOCK_DGRAM)
udp_sock.bind(("0.0.0.0", 8868))
tcp_sock = socket()
tcp_sock.bind(("0.0.0.0", 8888))
tcp_sock.listen(5)
f = open("16.txt", "r")
print("Monitor the start")
time.sleep(5)
rs, ws, xs = select([tcp_sock], [f], [])
print("rs:",rs)
print("ws:",ws)
print("xs:",xs)