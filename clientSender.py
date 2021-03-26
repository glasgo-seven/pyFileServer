import socket					# Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)				# Create a socket object
host = '192.168.1.8'	# '192.168.1.8'		# Get local machine name
port = 9170					# Reserve a port for your service.
print('Connecting to Server ...')

s.connect((host, port))
print(f'Connected to [{host}] port [{port}] !')

filename = 'sample.json'
f = open(filename,'rb')
l = f.read(1024)
while (l):
	s.send(l)
	l = f.read(1024)
f.close()

print('File is sent.')
s.close()
