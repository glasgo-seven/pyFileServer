from sys import argv
import socket													# Import socket module

if len(argv) == 5:												# > python clientSender.py host port filename
	if argv[1] == 'send':
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		# Create a socket object
		host = argv[2]												# Get server machine name
		port = int(argv[3])											# Reserve a port for your service.
		print('\nConnecting to Server ...')

		s.connect((host, port))
		print(f'Connected to [{host}] port [{port}] !')

		print('\tSending file ...')
		filename = argv[4]
		f = open(filename,'rb')
		l = f.read(1024)
		while (l):
			s.send(l)
			l = f.read(1024)
		f.close()

		print('\tFile is sent.')
		s.close()
		print('Connection closed.\n')
	elif argv[1] == 'recv':
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		# Create a socket object
		host = argv[2]												# Get server machine name
		port = int(argv[3])											# Reserve a port for your service.
		print('\nConnecting to Server ...')

		s.connect((host, port))
		print(f'Connected to [{host}] port [{port}] !')

		with open(argv[4], 'wb') as f:
			print('\tFile opened.')
			while True:
				print('\tReceiving data ...')
				data = s.recv(1024)
				if not data:
					break
				f.write(data)

		f.close()
		print('\tFile successfully recieved.')
		s.close()
		print('Connection closed.\n')
	else:
		print('\nWrong action!\nUse "send" or "recv".\n')
else:
	print('\nNot enough info!\nUse "> python client.py send/recv host port filename" format.\n')
