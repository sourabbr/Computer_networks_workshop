#!/usr/bin/python
import socket
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--ip', '-i', help='specify server ip address', required=True, action='store')
parser.add_argument('--port', '-p', help='specify server port number', required=True, type=int, action='store')
parser.add_argument('--sleep', '-s', help='specify sleep time in seconds', type=int, default =0, action='store')
parser.add_argument('--recv', '-r', help='specify bytes to receive from the socket', type=int, default=4096, action='store')
args = parser.parse_args()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (args.ip, args.port)
print('Listening on %s port %s' %server_address)
sock.bind(server_address)
sock.listen(5)

while True:
	connection, address = sock.accept() # Waiting for a connection to be accepted
	try:
#		print('connection from %s' %str(address))
		while True:
			data = connection.recv(args.recv)
			#print('received: %s' %data)
			if data:
				time.sleep(args.sleep)
				connection.sendall(data) #send the data back
			else:
				break
	finally:
		connection.close()
