import http.client
import json

SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/ping'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server: {SERVER}")
print(f"URL : {URL}")

#Connect with the server
conn = http.client.HTTPConnection(SERVER)
