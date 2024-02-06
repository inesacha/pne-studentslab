from pathlib import Path

FILENAME = "sequences/U5.fa"

file_contents = Path(FILENAME).read_text()

header = file_contents.find("\n")

body = file_contents[header:]

print(body)

#otra forma de hacerlo
#list_contents = file_contents.split("\n")
#for i in range(1, len(list_contents)
#   print(list_contents[i])