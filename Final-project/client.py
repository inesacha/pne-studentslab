import http.client
import json

SERVER = 'localhost'
PORT = 8080

conn = http.client.HTTPConnection(SERVER, port=PORT)


#listspecies
try:
    conn.request("GET", "/listSpecies?limit=10&json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()
response = conn.getresponse()
print(f"Response received!: {response.status} {response.reason}\n")
if response.status == 200:
    data_str = response.read().decode()
    data = json.loads(data_str)
   # print(data)
    total_number = data['total_number']
    print(f"There are {total_number} species in Ensembl.")
    if 'client_limit' in data:
        limit = data['client_limit']
        print(f'But you have select to show only {limit}.')
    print('The name of the species are: ')
    for s in data['name_species']:
        print(s)
