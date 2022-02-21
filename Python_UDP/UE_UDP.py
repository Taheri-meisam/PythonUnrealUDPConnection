#!/usr/bin/python3

import _thread
from socket import *

 
BUFF = 1024
HOST = '127.0.0.1'
PORT = 5001
def response(key):
    return 'Recieved'
 
def handler(clientsock,addr):
    while 1:
        data = clientsock.recv(BUFF)
        print ('data:' + repr(data))
        
        if not data: break
 

def sending(clientsock,addr):
    while 1:
        clientsock.sendto("919191",None,addr)
        
if __name__=='__main__':
    ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversock.bind(ADDR)
    serversock.listen(5)
    while 1:
        print ('waiting for connection...')
        clientsock, addr = serversock.accept()
        print ('...connected from:', addr)
        _thread.start_new_thread(handler(clientsock, addr))
        _thread.start_new_thread(sending(clientsock, addr))
