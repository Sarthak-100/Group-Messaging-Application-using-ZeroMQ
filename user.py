import zmq
import uuid

class User:
    def __init__(self, name,message_server_ip,uuid):
        self.name = name
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect(f"tcp://{message_server_ip}")
        self.uuid = uuid

    def get_group_list(self):
        self.socket.send_json({'request': 'GET_GROUP_LIST', 'uuid': self.uuid})
        response = self.socket.recv_json()
        print("\n".join([f"{name} - {ip_address}" for name, ip_address in response.items()]))

    def join_group(self,grp_port):
        grp_socket = zmq.Context().socket(zmq.REQ)
        grp_socket.connect(f"tcp://localhost:{grp_port}")
        grp_socket.send_json({'request': 'JOIN', 'uuid': self.uuid, 'name': self.name})
        response = grp_socket.recv_string()
        return response

    def leave_group(self,grp_port):
        grp_socket = zmq.Context().socket(zmq.REQ)
        grp_socket.connect(f"tcp://localhost:{grp_port}")
        grp_socket.send_json({'request': 'LEAVE', 'uuid': self.uuid})
        response = grp_socket.recv_string()
        return response

    def get_messages(self, timestamp=None):
        self.socket.send_json({'request': 'GET_MESSAGES', 'uuid': self.uuid, 'timestamp': timestamp})
        response = self.socket.recv_json()
        return response

    def send_message(self, message):
        self.socket.send_json({'request': 'SEND_MESSAGE', 'uuid': self.uuid, 'message': message})
        response = self.socket.recv_string()
        return response

if __name__ == "__main__":
    user = User("User1","localhost:2000",str(uuid.uuid1()))

    while True:
        print("\nMenu:")
        print("1. Get group list")
        print("2. Join group")
        print("3. Leave group")
        print("4. Get messages")
        print("5. Send message")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            user.get_group_list()
        elif choice == '2':
            grp_port = input("Enter group port to join: ")
            response = user.join_group(grp_port=int(grp_port))
            if response == "SUCCESS":
                print("Successfully joined group with port", grp_port)
        elif choice == '3':
            grp_port = input("Enter group port to leave: ")
            response = user.leave_group(grp_port=int(grp_port))
            if response == "SUCCESS":
                print("Successfully left group with port", grp_port)
        elif choice == '4':
            timestamp = input("Enter timestamp (leave blank for all messages): ")
            user.get_messages(timestamp)
        elif choice == '5':
            message = input("Enter your message: ")
            user.send_message(message)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
