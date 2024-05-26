from Seq1 import Seq
print("-----| Practice 1, Exercise 9 |------")
# -- Create a Null sequence
s = Seq()

# -- Initialize the null seq with the given file in fasta format
s.read_fasta("U5")

print(f"Sequence : (Length: {s.len()}) {s} \n  Bases: {s.count()}\n  Rev:   {s.reverse()}\n  Comp:  {s.complement()}")
