#!/usr/bin/python
import socket
import time
import os
import argparse
import multiprocessing

def perform():
    while True:
    	connection, address = sock.accept() #waiting for a connection to be accepted
    	try:
    		print('Child %s got a connection from %s' %(os.getpid(), address))
    		while True:
    			data = connection.recv(args.recv) #received data
                #print('received: %s' %data)
    			if data:
    				time.sleep(args.sleep)
    				connection.sendall(data) #send the data back
    			else:
    				break
    	finally:
            print('Child %s is done' %(os.getpid()))
            connection.close()

parser = argparse.ArgumentParser()
parser.add_argument('--ip', '-i', help='specify server ip address', required=True, action='store')
parser.add_argument('--port', '-p', help='specify server port number', required=True, type=int, action='store')
parser.add_argument('--sleep', '-s', help='specify sleep time in seconds', type=int, default=0, action='store')
parser.add_argument('--recv', '-r', help='specify bytes to receive from the socket', type=int, default=4096, action='store')
args = parser.parse_args()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (args.ip, args.port) #server ip and port
print('Listening on %s port %s' %server_address)
sock.bind(server_address)
sock.listen(5)

p1 = multiprocessing.Process(target=perform)
p1.start()
p2 = multiprocessing.Process(target=perform)
p2.start()
#p3 = multiprocessing.Process(target=perform3)
#p3.start()
