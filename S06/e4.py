from seq01 import *
import termcolor

def generate_seqs(pattern, number):
    seq_list = []
    for i in range(1, number +1):
        seq_list.append(Seq(pattern * i)) #hace que sea objet
    return seq_list


def print_seqs(seq_list, color):
    i = 0
    for s in seq_list:
        termcolor.cprint(f"Sequence {i} Length: {s.len()}) {s}", color)
        i += 1


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", 'blue')
print_seqs(seq_list1, 'blue')

termcolor.cprint("List 2:", 'green')
print_seqs(seq_list2, 'green')
