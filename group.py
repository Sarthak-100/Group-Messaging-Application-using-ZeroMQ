import zmq

class GroupServer:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.connect(f"tcp://{ip}")

    def start(self):
        while True:
            message = self.socket.recv_string()
            print(f"JOIN REQUEST FROM {message}")
            # Handle join request, add user to USERTELE, and send SUCCESS response
            self.socket.send_string("SUCCESS")

if __name__ == "__main__":
    server = GroupServer("GroupName", "127.0.0.1:1234")
    server.start()
