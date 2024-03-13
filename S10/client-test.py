
from Client0 import Client

PORT = 8081
IP = "127.0.0.1"
c = Client(IP, PORT)
for i in range(5):
    c.talk(f"Message {i}")