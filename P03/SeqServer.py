import socket
import termcolor
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
                print("SEQ Server configured!")
                print("Waiting for clients...")
                (clientsocket, address) = serversocket.accept()

                # Read the message from the client, if any
                msg = clientsocket.recv(2048).decode("utf-8")
                # Send the message
                response = self.what_appears_on_clients_and_on_servers(msg)
                send_bytes = str.encode(response)
                # We must write bytes, not a string
                clientsocket.send(send_bytes)

                clientsocket.close()

        except socket.error:
            print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(IP, PORT))

        except KeyboardInterrupt:
            print("Server stopped by the user")
            serversocket.close()

    def what_appears_on_clients_and_on_servers(self, msg):
        if msg.startswith("PING"):
            termcolor.cprint("PING command!", "green")
            return "OK!\n"

        elif msg.startswith("GET"):
                termcolor.cprint("GET", 'green')
                get = self.get_function(msg)
                print(get)
                return get

        elif msg.startswith("INFO"):
            termcolor.cprint("INFO", 'green')
            info = self.info_function(msg)
            print(info)
            return info

        elif msg.startswith("COMP"):
            termcolor.cprint("COMP", 'green')
            comp = self.comp_function(msg)
            print(comp)
            return comp

        elif msg.startswith("REV"):
            termcolor.cprint("REV", 'green')
            rev = self.rev_function(msg)
            print(rev)
            return rev

        elif msg.startswith("GENE"):
            termcolor.cprint("GENE", 'green')
            gene = self.gene_function(msg)
            print(gene)
            return gene

    def get_function(self, msg):
        which_gene_to_send = msg.split(" ")
        try:
            gene_to_send = int(which_gene_to_send[1])
            genes = ['ACGTTT', 'AAAAGTCGTC', 'ACGTTT', 'ACGTACGTA', 'ACGT']
            g = genes[gene_to_send]
            return g
        except IndexError:
            return "Insert a valid sequence"

    def info_function(self, msg):
        gene = msg.split(" ")
        try:
            gene = gene[1]
            seq = Seq(gene) #tenes que pasar por el constructor(llamar al init), seq seria un objeto del tipo que queres importante volverla un objeto de Seq para poder usar los metodos de la clase Seq
            result = f"Sequence: {seq} \nTotal length: {seq.len()}"
            result += f"\nA:{seq.count_base('A')} ({seq.count_base('A') / round(seq.len() * 100, 1)}%)"
            result += f"\nC:{seq.count_base('C')} ({seq.count_base('C') / round(seq.len() * 100, 1)}%)"
            result += f"\nG:{seq.count_base('G')} ({seq.count_base('G') / round(seq.len() * 100, 2)}%)"
            result += f"\nT:{seq.count_base('T')} ({seq.count_base('T') / round(seq.len() * 100, 2)}%)"
        except IndexError:
            result = "Insert a valid sequence"
        return result

    def comp_function(self, msg):
        seq = msg.split(" ")
        try:
            seq = seq[1]
            seq = Seq(seq)
            comp = seq.complement()
        except IndexError:
            comp = "Insert a valid sequence"
        return comp

    def rev_function(self, msg):
        seq = msg.split(" ")
        try:
            seq = seq[1]
            seq = Seq(seq)
            rev = seq.reverse()
        except IndexError:
            rev = "Insert a valid sequence"
        return rev

    def gene_function(self, msg):
        which_gene_to_send = msg.split(" ")
        try:
            gene_to_send = which_gene_to_send[1]
            seq = Seq()
            return seq.read_fasta(gene_to_send)
        except IndexError:
            return "Insert a valid sequence"


c = Server()

