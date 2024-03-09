import socket
import termcolor
from pathlib import Path
from Seq1 import *


class Server:

    def __init__(self):
        # Configure the Server's IP and PORT
        PORT = 8080
        IP = "127.0.0.1"
        # create an INET, STREAMing socket
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            serversocket.bind((IP, PORT))
            # become a server socket
            # MAX_OPEN_REQUESTS connect requests before refusing outside connections
            serversocket.listen()

            while True:
                # accept connections from outside
                print("Waiting for clients...")
                (clientsocket, address) = serversocket.accept()

                # Read the message from the client, if any
                msg = clientsocket.recv(2048).decode("utf-8")
                # Send the message
                response = self.what_appears_on_clients(msg)
                send_bytes = str.encode(response)
                # We must write bytes, not a string
                clientsocket.send(send_bytes)

                clientsocket.close()

        except socket.error:
            print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(IP, PORT))

        except KeyboardInterrupt:
            print("Server stopped by the user")
            serversocket.close()


    def what_appears_on_clients(self, msg):
        if msg.startswith("PING"):
            termcolor.cprint("PING command!", "green")
            return "OK!\n"

        elif msg.startswith("GET"):
            which_gene_to_send = msg.split(" ")
            gene_to_send = which_gene_to_send[1]
            genes = ['ADA', 'FRAT1', 'FXN', 'U5','RNU6_269P']
            i = 0
            for g in genes:
                if str(i) == gene_to_send:
                    termcolor.cprint("GET", 'green')
                    print(self.read_fasta(g))
                    return self.read_fasta(g)
                i += 1

        elif msg.startswith("INFO"):
            gene = msg.split(" ")
            gene = gene[1]
            seq = Seq(gene)
            length = f"Total length: {seq.len()}"
            c_a = f"\nA:{seq.count_base('A')} ({seq.count_base('A') / seq.len() * 100}%)"
            c_c = f"\nC:{seq.count_base('C')} ({seq.count_base('C') / seq.len() * 100}%)"
            c_g = f"\nG:{seq.count_base('G')} ({seq.count_base('G') / seq.len() * 100}%)"
            c_t = f"\nT:{seq.count_base('T')} ({seq.count_base('T') / seq.len() * 100}%)"
            termcolor.cprint("INFO", 'green')
            print(f"Sequence: {seq}{length} {c_a}, {c_c}, {c_g}, {c_t}")
            return f"Sequence: {seq}{length} {c_a}, {c_c}, {c_g}, {c_t}"

    def get_function(self, msg):





c = Server()

