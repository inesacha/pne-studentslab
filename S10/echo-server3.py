import socket
import termcolor
from Client0 import Client

PORT = 8081
IP = "" # this IP address is local, so only requests from the same machine are possible

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening, server ready to listen different request
ls.listen()

print("The server is configured!")

i = 0
clients_list = []
number_con = 0
flag = True
while flag:
    number_con += 1
    (rs, address) = ls.accept()
    print("Waiting for Clients to connect")
    print(f"A client has connected to the server!")
    Msg = f"CONNECTION {number_con}. Client IP,PORT: {address}"
    rs.send(Msg.encode())
    msg = rs.recv(2048).decode("utf-8")
    print("Message received: " + termcolor.colored(msg, "green"))
    newMsg = termcolor.colored(f"Message{i}", "green")
    rs.send(newMsg.encode())
    rs.close()
    i += 1
    clients_list.append(address)
    if number_con == 5:
        flag = False


message = "The following clients has connected to server"
rs.send(message.encode())
for i in range(len(clients_list)):
    message = f"Client {i}: {clients_list[i]}"
    rs.send(message.encode())
# -- Close the socket
ls.close()
