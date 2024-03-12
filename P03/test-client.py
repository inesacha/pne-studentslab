from Client0 import *
PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

PORT = 8080
IP = "127.0.0.1"
c = Client(IP, PORT)
print(c)
print("* Testing PING...")
response = c.talk("PING")
print(response)

print("* Testing GET...")
for n in range(5):
    response = c.talk(f"GET {n}")
    print(f"GET {n}: {response}")

print("\n* Testing INFO...")
response = c.talk("INFO ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")
print(f"INFO {response}")

print("\n* Testing COMP...")
response = c.talk("COMP ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCATGGAGGAGAGGTCGTTACGGTTGGGGTCAGGTCCGGGGGTAGGCGGGTCCTAGAGCTAGT")
print(f"COMP {response}")

print("\n* Testing REV...")
response = c.talk("REV ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCAACTAGCTCTAGGACCCGCCTACCCCCGGACCTGACCCCAACCGTAACGACCTCTCCTCCA")
print(f"REV {response}")

print("\n* Testing GENE...")
gene = ["U5","ADA", "FRAT1", "FXN", "RNU6_269P"]
for g in gene:
    print(f"GENE {g}")
    response = c.talk(f"GENE {g}")
    print(response)

