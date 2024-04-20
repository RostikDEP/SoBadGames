import socket
import json
import threading

class Server:
    def __init__(self):
        self.server = None
        self.ip = None
        self.port = None
        self.listening = True
        self.LoadConfigurations()

    def LoadConfigurations(self):
        with open("configuration.json", 'r', encoding='utf-8') as config_file:
            config_json = json.load(config_file)
            self.ip, self.port = config_json['server_host']['ip'], int(config_json['server_host']['port'])

    def Bind(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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


if __name__ == "__main__":
    server = Server()
    server.Bind()
    server.StartListeningLoop()
