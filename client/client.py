import socket
import time
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

login = input("Enter login: ")
client.connect(('109.108.241.14', 4747))
client.send(login.encode())
status = client.recv(2).decode()
if status == "OK":
    client.send(b"request")
