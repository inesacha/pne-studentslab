class Seq:
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence is created!")
    def __str__(self):
        return self.strbases
    def len(self):
        return len(self.strbases)

def generate_seqs(pattern, number):
    seq_list = []
    for i in range(1, number +1):
        seq_list.append(Seq(pattern * i)) #hace que sea objet

    return seq_list

def print_seqs(seq_list):
    i = 0
    for s in seq_list:
        print(f"Sequence", i, ": (Length:", s.len(), ")", s)
        i += 1

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)
