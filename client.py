import socket

#HOST = '217.147.184.143'
HOST = '10.30.9.255'
PORT = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("Hello, server!".encode('utf-8'))

print(socket.recv(1024).decode('utf-8'))