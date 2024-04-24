import http.client
import json
import termcolor

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", "/listusers")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
person = json.loads(data1)

print("CONTENT: ")

peopleNumbers = person['People']


termcolor.cprint("Total people in the database: ", 'green', end='')
print(len(peopleNumbers))


print()
for i, dictnum in enumerate(person['People']):
    termcolor.cprint("Name: ", 'green', end="")
    print(person['People'][i]['Firstname'], person['People'][i]['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(person['People'][i]['age'])
    phoneNumbers = person['People'][i]['phoneNumber']
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))
    for i, dictnum in enumerate(phoneNumbers):
        termcolor.cprint("  Phone " + str(i) + ": ", 'blue')
        # The element num contains 2 fields: number and type
        termcolor.cprint("\t Type: ", 'red', end='')
        print(dictnum['type'])
        termcolor.cprint("\t Number: ", 'red', end='')
        print(dictnum['number'])
