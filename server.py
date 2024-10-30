import threading
import socket

# practice 

HOST = '10.30.9.255'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5) 

while True:
    communication_socket, address = server.accept()
    print(f"Connection from {address} has been established!")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from client: {message}")
    communication_socket.send("Message received!".encode('utf-8'))
    communication_socket.close()
    print(f"Connection from {address} has been closed!")
