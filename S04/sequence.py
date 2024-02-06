from pathlib import Path

FILENAME = "sequences/ADA.fa"

file_contents = Path(FILENAME).read_text()

list_contents = file_contents.split("\n")

list_contents.pop(0)

print(len("".join(list_contents)))

#hay otra forma de hacerlo como lo haciamos antes
