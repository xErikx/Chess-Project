import socket
from UserClass import UserCommunication

SERVER_IP = "127.0.0.1"
PORT = 4040
ADDR = (SERVER_IP, PORT)


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDR)


player_communication = UserCommunication(client_socket)

status = True

while True:
    receiving_msg = player_communication.receiving_msg()
    print(receiving_msg)    # ["msg"]
    player_input = input(": ")
    player_communication.send_msg({"msg": player_input})

