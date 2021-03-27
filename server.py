import socket													# Import socket module
from datetime import datetime

host = socket.gethostbyname(socket.gethostname())				# Get local machine name


portFrom = 9170													# Reserve a port for your service.
sFrom = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		# Create a socket object
sFrom.bind((host, portFrom))									# Bind to the port

sFrom.listen(1)													# Now wait for client connection.
print(f'\nServer [{host}] is listening on [{portFrom}] port ...')
conn, addr = sFrom.accept()										# Establish connection with client.

print(f'Got connection from {addr} !')
filename = datetime.now().strftime("clientFile_%m%d%Y_%H%M%S")

with open(filename, 'wb') as f:
	print('\tFile opened.')
	while True:
		print('\tReceiving data ...')
		data = conn.recv(1024)
		if not data:
			break
		f.write(data)
f.close()
print('\tFile successfully recieved.')
conn.close()
sFrom.close()
print(f'Socket at port {portFrom} closed.')


portTo = 9150
sTo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sTo.bind((host, portTo))

sTo.listen(1)
print(f'\nServer [{host}] is listening on [{portTo}] port ...')
conn, addr = sTo.accept()

print(f'Got connection from {addr} !')
print('\tSending file ...')
f = open(filename,'rb')
l = f.read(1024)
while (l):
	conn.send(l)
	l = f.read(1024)
f.close()
print('\tFile is sent.')
conn.close()
sTo.close()
print(f'Socket at port {portTo} closed.')


print('\nServer is shuted down.\n')
