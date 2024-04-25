import http.client
import json
import termcolor
from Seq1 import Seq

genes = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}


NAME = str(input("Write the gene name:"))
SERVER = 'rest.ensembl.org'
ENDPOINT = f'/sequence/id/{genes[NAME]}'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server: {SERVER}")
print(f"URL : {URL}")


conn = http.client.HTTPConnection(SERVER)


try:
    conn.request("GET", ENDPOINT + PARAMS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

gene = json.loads(data1)

print()
termcolor.cprint("Gene: ", 'green', end="")
print(NAME)

termcolor.cprint("Description: ", 'green', end="")
print(gene['desc'])

s = Seq(gene['seq'])
termcolor.cprint("Total length: ", 'green', end="")
print(s.len())

termcolor.cprint("A", 'blue', end="")
print(f": {s.count_base('A')} ({round((s.count_base('A') / s.len() * 100),1)}%)")
termcolor.cprint("C", 'blue', end="")
print(f": {s.count_base('C')} ({round((s.count_base('C') / s.len() * 100),1)}%)")
termcolor.cprint("G", 'blue', end="")
print(f": {s.count_base('G')} ({round((s.count_base('G') / s.len() * 100),1)}%)")
termcolor.cprint("T", 'blue', end="")
print(f": {s.count_base('T')} ({round((s.count_base('T') / s.len() * 100),1)}%)")

termcolor.cprint("Most frequent Base", 'green', end="")
print(f": {s.processing_the_genes(NAME)}")