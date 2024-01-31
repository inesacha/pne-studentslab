sequence = input("Enter a sequence:")
c_a = 0
c_c = 0
c_t = 0
c_g = 0
for i in sequence.lower():
    if i == "a":
        c_a += 1
    elif i == "c":
        c_c += 1
    elif i == "t":
        c_t += 1
    elif i == "g":
        c_g = 1
print("Introduce the sequence:", sequence, "\n Total length:", len(sequence), "\nA:", c_c, "\nC:", c_c"