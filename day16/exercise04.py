# author:xiao kun time:5/12/22
import select
from select import *
from socket import *


tcp_sock = socket()
tcp_sock.bind(("0.0.0.0", 8888))
tcp_sock.listen(5)
tcp_sock.setblocking(False)
p = epoll()
p.register(tcp_sock,POLLIN)
map = {tcp_sock.fileno():tcp_sock}

while True:
    events = p.poll()
    for fd, event in events:
        if fd == tcp_sock.fileno():
            print(fd)
            connfb, address = map[fd].accept()
            print("Connect From:", address)
            connfb.setblocking(False)
            p.register(connfb,EPOLLIN|EPOLLERR)
            map[connfb.fileno()] = connfb
        elif event == POLLIN:
            data = map[fd].recv(1024).decode()

            if not data:
                p.unregister(fd)
                map[fd].close()
                del map[fd]
                continue
            print(data)
            map[fd].send(b"OK")