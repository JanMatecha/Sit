#priklady z http://www.binarytides.com/python-socket-programming-tutorial/

# Socket client example in python

# handling errors in python socket programs

import socket  # for sockets
import sys  # for exit

try:
    # create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print(e)
    #print('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
    sys.exit()

print('Socket Created')

host = 'www.google.com'
port = 80


try:
    remote_ip = socket.gethostbyname(host)

except socket.gaierror:
    # could not resolve
    print('Hostname could not be resolved. Exiting')
    sys.exit()

print('Ip address of ' + host + ' is ' + remote_ip)

# Connect to remote server
s.connect((remote_ip, port))

print('Socket Connected to ' + host + ' on ip ' + remote_ip)

# Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"

try:
    # Set the whole string
    # s.sendall(message) nefunguje, priklad pro python 2
    # message.encode('utf-8') a zpet message.decode('utf-8') by mohlo pomoct
    s.sendall(message.encode())
except socket.error:
    # Send failed
    print('Send failed')
    sys.exit()

print('Message send successfully')

# Now receive data
reply = s.recv(4096)

print(reply.decode('utf-8'))

s.close()
