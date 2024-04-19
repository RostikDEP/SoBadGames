import socket
import json


class Server:
    def __init__(self):
        self.ip = None
        self.port = None
        self.server = None
        self.LoadConfigurations()

    def LoadConfigurations(self):
        with open("configuration.json", 'r', encoding='utf-8') as config_file:
            config_json = json.load(config_file)
            self.ip, self.port = config_json['server_host']['ip'], int(config_json['server_host']['port'])

    def Bind(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, self.port))


if __name__ == "__main__":
    server = Server()
    server.Bind()