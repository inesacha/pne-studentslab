from P02.Seq1 import Seq
print("-----| Practice 1, Exercise 10 |------")

genes = ['U5', 'ADA', 'FRAT1', 'FXN', 'RNU6_269P']
for g in genes:
    s = Seq()
    s.read_fasta(g)
    print(f"Gene {g}: Most frequent Base: {s.processing_the_genes(g)}")