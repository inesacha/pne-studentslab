import socket

PORT = 8081
IP = ""

while True:
    # -- Ask the user for the message
    message = input("Write a message:")

    # -- Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # -- Establish the connection to the Server
    s.connect((IP,PORT))

    # -- Send the user message
    s.send(str.encode(message))

    # -- Close the socket
    s.close()
