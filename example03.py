#priklady z http://www.binarytides.com/python-socket-programming-tutorial/

import socket
import sys

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 5000  # Arbitrary non-privileged port

# create an AF_INET, STREAM socket (TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')



try:
    s.bind((HOST, PORT))
except socket.error as e:
    print('Bind failed. ')
    #TODO> Error Code a Message
    print(e)
    sys.exit()

print('Socket bind complete')

s.listen(10)
print('Socket now listening')

# now keep talking with the client
while 1:
    # wait to accept a connection - blocking call
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))

    data = conn.recv(1024)
    reply = 'OK...' + data.decode('utf-8')
    print(reply)
    if not data:
        break

    conn.sendall(reply.encode())

conn.close()
s.close()

