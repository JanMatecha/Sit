#https://pymotw.com/2/socket/tcp.html
#client


import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
#print >>sys.stderr, 'connecting to %s port %s' % server_address
print ('connecting to %s port %s' % server_address, file = sys.stderr)

sock.connect(server_address)

try:

    # Send data
    message = 'This is the message.  It will be repeated.'
    #print >> sys.stderr, 'sending "%s"' % message
    print('sending "%s"' % message, file=sys.stderr)


    sock.sendall(message.encode())

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        #print >> sys.stderr, 'received "%s"' % data
        print('received "%s"' % data.decode('utf-8'), file=sys.stderr)

finally:
    #print >> sys.stderr, 'closing socket'
    print('closing socket', file=sys.stderr)
    sock.close()

