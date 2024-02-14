class Seq:
    def __init__(self, strbases):
        self.strbases = strbases
    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

def print_seqs(seq_list):
    i = 0
    for s in seq_list:
        print(f"Sequence", i, ": (Length:", s.len(), ")", s)
        i += 1

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

print(print_seqs(seq_list))
