# client.py

import socket					# Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)				# Create a socket object
host = '192.168.1.8'		# Get local machine name
port = 9150					# Reserve a port for your service.
print('Connecting to Server...')

s.connect((host, port))
print(f'Connected to [{host}] port [{port}]')

with open('receivedFromServer.json', 'wb') as f:
	print('file opened')
	while True:
		print('receiving data...')
		data = s.recv(1024)
		if not data:
			break
		f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')