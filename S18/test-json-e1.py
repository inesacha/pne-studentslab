import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-e1.json").read_text()

# Create the object person from the json string
person = json.loads(jsonstring)

# Get the people's list
peopleNumbers = person['People']

# Print the number of people in the list
termcolor.cprint("Total people in the database: ", 'green', end='')
print(len(peopleNumbers))

# Print the information on the console, in colors
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

