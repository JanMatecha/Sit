#priklady z http://www.binarytides.com/python-socket-programming-tutorial/

import socket
import sys

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 8888  # Arbitrary non-privileged port

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

# wait to accept a connection - blocking call
conn, addr = s.accept()

# display client information
print('Connected with ' + addr[0] + ':' + str(addr[1]))

# now keep talking with the client
while True:
    data = conn.recv(1024)
    print (data.decode('utf-8'))
    conn.sendall(data)

conn.close()
s.close()

