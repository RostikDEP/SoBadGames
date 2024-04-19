import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('109.108.241.14', 1212))

server.listen()
client, address = server.accept()
# data = client.recv(1024).decode()
# print(data)