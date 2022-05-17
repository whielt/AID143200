# author:xiao kun time:5/12/22
import socket
import time
from socket import *

ADDR = ("0.0.0.0", 8888)
sockfb = socket()
sockfb.bind(ADDR)
sockfb.listen(5)
# sockfb.setblocking(False)
sockfb.settimeout(3.0)
while True:
    print("Waiting from accept")
    try:
        connfb, addr = sockfb.accept()
        print("Connect from:", addr)
    except (BlockingIOError,timeout) as e:
        with open("date.txt", "w") as d:
            d.write("%s,%s" % (time.ctime(), e))
        time.sleep(2)
    else:
        message = connfb.recv(128).decode()
        print(message)
