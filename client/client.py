import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('109.108.241.14', 1212))

client.send("CHECK".encode())