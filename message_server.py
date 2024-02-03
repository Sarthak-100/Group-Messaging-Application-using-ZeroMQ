import zmq

class MessageServer:
    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind("tcp://127.0.0.1:2000")

    def start(self):
        while True:
            message = self.socket.recv_string()
            print(f"JOIN REQUEST FROM {message}")
            # Handle join request, register group server, and send SUCCESS response
            self.socket.send_string("SUCCESS")

if __name__ == "__main__":
    server = MessageServer()
    server.start()
