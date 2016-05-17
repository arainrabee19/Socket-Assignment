# Socket-Assignment

import socket  # Import socket module
from thread import *

s = socket.socket()
host = socket.gethostname()
port = 5173  # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)

def receive():
    while True:
        data=s.recv(1024)
        print data

start_new_thread(receive, ())
while 1:
    rep=raw_input()
    s.send(rep)
    if not rep:
        break



s.close
