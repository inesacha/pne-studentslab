class Seq:
    def __init__(self, strbases):
        count = 0
        for s in strbases:
            if s == "A":
                count += 1
            elif s == "C":
                count += 1
            elif s == "G":
                count += 1
            elif s == "T":
                count += 1
        if count != len(strbases):
            self.strbases = "ERROR"
            print("ERROR!!")
        else:
            self.strbases = strbases
            print("New sequence is created")
    def __str__(self):
        return self.strbases

#no hace falta count, podes hacer directo que da prblema si no es
s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")

