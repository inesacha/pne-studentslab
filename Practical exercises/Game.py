import random
import socket


class NumberGuesser:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = []


    def guess(self, number):
        if int(number) == self.secret_number:
            hint = f"You won after {len(self.attempts)} attempts."
        elif int(number) < self.secret_number:
            self.attempts.append(number)
            hint = "Higher\n"
        elif int(number) > self.secret_number:
            self.attempts.append(number)
            hint = "Lower\n"

        return hint


PORT = 8080
IP = "127.0.0.1"

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((IP, PORT))
serversocket.listen()
ng = NumberGuesser()
print("Game on")
flag = True
while flag:
    (clientsocket, address) = serversocket.accept()
    print("A client is connected")
    print("Try your guess")
    msg = clientsocket.recv(2048).decode("utf-8")
    print(msg)
    response = ng.guess(msg)
    print(response)
    send_bytes = str.encode(response)
    clientsocket.send(send_bytes)
    if response.startswith("You"):
        flag = False
clientsocket.close()








