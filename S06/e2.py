from seq01 import Seq


def print_seqs(seq_list):
    for s in seq_list:
        print(f"Sequence {seq_list.index(s)}: (Length: {s.len()}) {s}")


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")] #lo de adentro son objetos
print_seqs(seq_list)

