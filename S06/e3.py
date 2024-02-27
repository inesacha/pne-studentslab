from seq01 import Seq
def generate_seqs(pattern, number):
    seq_list = []
    for i in range(1, number +1):
        seq_list.append(Seq(pattern * i))

    return seq_list


def print_seqs(seq_list):
    i = 0
    for s in seq_list:
        print(f"Sequence {i} Length: {s.len()}) {s}")
        i += 1


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)
