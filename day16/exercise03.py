# author:xiao kun time:5/12/22
from select import select
from socket import *

tcp_sock = socket()
tcp_sock.bind(("0.0.0.0", 8888))
tcp_sock.listen(5)
tcp_sock.setblocking(False)
rlixt = [tcp_sock]
wlixt = []
xlixt = []
while True:
    rs, ws, xs = select(rlixt, wlixt, [])
    for r in rs:
        if r is tcp_sock:
            connfb, address = tcp_sock.accept()
            connfb.setblocking(False)
            print("Connect From:", address)
            rlixt.append(connfb)
        else:
            data = r.recv(1024).decode()
            if not data:
                rlixt.remove(r)
                r.close()
                continue
            print(data)
            wlixt.append(r)
    for w in ws:
        w.send(b"OK")
        wlixt.remove(w)


