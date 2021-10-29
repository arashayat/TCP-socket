from socket import *
import webbrowser

serverName = 'localhost'
serverPort = 12110
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

file_name = input('Please Enter the url: ')
file_path = input('please enter the path of file: ')
file_msg = str.encode(f'{file_path}/{file_name}.html')

clientSocket.send(file_msg)
response = clientSocket.recv(2048).decode()

if response == '200':
    print('200 OK')
    http_file = clientSocket.recv(2048)
    print(http_file.decode())

elif response == '404':
    print('404 Not Found')
else:
    print('500 Internal Server Error')

clientSocket.close()