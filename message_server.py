import zmq

class MessageServer:
    def __init__(self, port):
        self.port = port
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind(f"tcp://*:{self.port}")
        self.groups = {}

    def register_group(self, name, port):
        if name not in self.groups:
            self.groups[name] = port
            return "SUCCESS"
        else:
            return "FAILURE: Group already exists"
    
    def get_group_list(self):
        return self.groups

    def start(self):
        print("Message Server started...")
        while True:
            message = self.socket.recv_json()
            if message['request'] == 'JOIN':
                response = self.register_group(message['name'], message['port'])
                print(f"JOIN REQUEST FROM {message['name']}: {message['port']}")
                self.socket.send_string(response)
                if response == "SUCCESS":
                    print("SUCCESS")
            elif message['request'] == 'GET_GROUP_LIST':
                print(f"GROUP LIST REQUEST FROM user {message['uuid']}")
                response = self.get_group_list()
                self.socket.send_json(response)

if __name__ == "__main__":
    server = MessageServer(2000)
    server.start()
