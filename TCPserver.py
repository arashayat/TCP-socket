from socket import *
from os.path import exists

serverPort = 12110
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(1)
print('server ready!')

while True:
    connectionSocket, addr = serverSocket.accept()
    file_path= connectionSocket.recv(2048)

    if exists(file_path):
        connectionSocket.send('200'.encode())
        file = open(file_path, 'r')

        connectionSocket.send(file.read().encode())
        connectionSocket.close()
    
    else:
        connectionSocket.send('404'.encode())
        connectionSocket.close()

