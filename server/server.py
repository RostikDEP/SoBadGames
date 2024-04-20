import socket
import json
import threading
import sys

class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = None
        self.port = None
        self.config_json = None
        self.listening = True
        self.LoadConfigurations()

    def LoadConfigurations(self):
        with open("configuration.json", 'r', encoding='utf-8') as config_file:
            config_json = json.load(config_file)
            self.config_json = config_json
            self.ip, self.port = config_json['server_host']['ip'], int(config_json['server_host']['port'])

    def Bind(self):
        self.server.bind((self.ip, self.port))
        self.server.listen()

    def StartListeningLoop(self):
        while self.listening:
            try:
                client, address = self.server.accept()
                thread = threading.Thread(target=self.HandleClient, args=(client, address))
                thread.start()
                print(f"Active connections: {threading.active_count() - 1}")
            except Exception as e:
                print("Error")

    def HandleClient(self, client, address):
        print(f"New connection: {address}")
        login = client.recv(10).decode()
        if login in self.config_json["supported_users"]:
            client.send(b"OK")
            print(f"Connected user: {login}")
            mode = client.recv(10).decode()

            if mode == "request":
                target = self.config_json["targets_network"][login]
                with open("tasks.json", "r") as file:
                    tasks_json = json.load(file)

                if len(tasks_json[target]["requests"]) != 0:
                    print(f"Target have requests: {str(tasks_json[target]["requests"])}")
                else:
                    print("Target haven't requests")

        else:
            print(f"User {login} is not supported")
            client.close()


if __name__ == "__main__":
    server = Server()
    server.Bind()
    server.StartListeningLoop()
