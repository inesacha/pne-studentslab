from Client0 import Client
from Seq1 import *
PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "212.128.255.64"
PORT = 8081
c = Client(IP, PORT)
print(c)
s = Seq()
GENES = ["U5", "FRAT1", "ADA"]
for gene in GENES:
    s.read_fasta(gene)
    msg = f"Sending {gene} Gene to the server..."
    print(msg)
    first_response = c.talk(msg)
    print(f"From server: {first_response}")
    msg2 = str(s)
    print(f"To server: {msg2}")
    second_response = c.talk(f"{msg2}")
    print(f"From server: {second_response}")

