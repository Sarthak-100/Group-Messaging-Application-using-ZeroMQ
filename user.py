import zmq

class User:
    def __init__(self, server_ip):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect(f"tcp://{server_ip}")

    def get_group_list(self):
        self.socket.send_string("GROUP LIST REQUEST")
        group_list = self.socket.recv_string()
        print(f"Group List: {group_list}")

    # Add methods for joinGroup, leaveGroup, getMessage, sendMessage

if __name__ == "__main__":
    user = User("127.0.0.1:2000")
    user.get_group_list()
