import zmq
import time
import threading

class GroupServer:
    def __init__(self, name, port, message_server_port):
        self.name = name
        self.port = port
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind(f"tcp://*:{self.port}")
        self.message_server_socket = self.context.socket(zmq.REQ)
        self.message_server_socket.connect(f"tcp://localhost:{message_server_port}")
        self.users = {}
        self.messages = []

    def join_message_server(self):
        self.message_server_socket.send_json({'request': 'JOIN', 'name': self.name, 'port': self.port})
        response = self.message_server_socket.recv_string()
        return response
    
    def handle_user_request(self):
        while True:
            message = self.socket.recv_json()
            if message['request'] == 'JOIN':
                self.users[message['uuid']] = message['name']
                print(f"Join request from User {message['uuid']}")
                print("User has successfully joined the group")
                self.socket.send_string("SUCCESS")
            elif message['request'] == 'LEAVE':
                del self.users[message['uuid']]
                print(f"Leave request from User {message['uuid']}")
                print("User has successfully left the group")
                self.socket.send_string("SUCCESS")
            elif message['request'] == 'GET_MESSAGES':
                timestamp = message.get('timestamp')
                messages_to_send = [msg for msg in self.messages if msg['timestamp'] >= timestamp] if timestamp else self.messages
                self.socket.send_json(messages_to_send)
            elif message['request'] == 'SEND_MESSAGE':
                if message['uuid'] in self.users:
                    self.messages.append({'uuid': message['uuid'], 'message': message['message'], 'timestamp': time.strftime('%H:%M:%S')})
                    self.socket.send_string("SUCCESS")
                else:
                    self.socket.send_string("FAILURE: User not in group")
    def start(self):
        threading.Thread(target=self.handle_user_request).start()

if __name__ == "__main__":
    port_num = int(input("Enter port number for group server: "))
    server_name = input("Enter group server name: ")
    group_server = GroupServer(server_name, port_num, 2000)
    print("Group Server "+group_server.name+" "+str(group_server.port)+" started...")
    response = group_server.join_message_server()
    print("join request response from message server : ",response)
    group_server.start()
