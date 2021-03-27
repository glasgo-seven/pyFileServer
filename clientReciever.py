from sys import argv
import socket													# Import socket module

if len(argv) == 4:												# > python clientReciever.py host port filename
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		# Create a socket object
	host = argv[1]												# Get server machine name
	port = int(argv[2])											# Reserve a port for your service.
	print('\nConnecting to Server ...')

	s.connect((host, port))
	print(f'Connected to [{host}] port [{port}] !')

	with open(argv[3], 'wb') as f:
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
	print('\nNot enough info!\nUse "> python clientReciever.py host port filename" format.\n')