from sys import argv
import socket													# Import socket module

if len(argv) == 4:												# > python clientSender.py host port filename
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		# Create a socket object
	host = argv[1]												# Get server machine name
	port = int(argv[2])											# Reserve a port for your service.
	print('\nConnecting to Server ...')

	s.connect((host, port))
	print(f'Connected to [{host}] port [{port}] !')

	print('\tSending file ...')
	filename = argv[3]
	f = open(filename,'rb')
	l = f.read(1024)
	while (l):
		s.send(l)
		l = f.read(1024)
	f.close()

	print('\tFile is sent.')
	s.close()
	print('Connection closed.\n')
else:
	print('\nNot enough info!\nUse "> python clientSender.py host port filename" format.\n')
