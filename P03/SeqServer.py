import socket
import termcolor
from pathlib import Path


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
            genes = ['ADA', 'FRAT1', 'FXN', 'U5']
            i = 0
            for g in genes:
                self.read_fasta(g)
                i += 1
                if str(i) == gene_to_send:
                    return g

    def read_fasta(self, filename):
        folder = "../sequences/"
        filename = filename + ".txt"
        file_contents = Path(folder + filename).read_text()
        header = file_contents.find("\n")
        body = file_contents[header:]
        list_contents = body.replace("\n", "")
        self.strbases = list_contents
        return self.strbases




c = Server()

