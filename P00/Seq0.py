from pathlib import Path
def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()

    header = file_contents.find("\n")

    body = file_contents[header:]

    list_contents = body.replace("\n", "")

    print("The first 20 bases are:")
    print(list_contents[:20])

def seq_len(seq):
    FOLDER = "../sequences/"
    FILENAME = seq + ".fa"
    file_contents = Path(FOLDER + FILENAME).read_text()
    header = file_contents.find("\n")
    body = file_contents[header:]

    list_contents = body.replace("\n", "")
    print("Gene", seq + "-> Length:", len(list_contents))

def seq_count_base(bases):
    #for g in genes:
     #   for b in bases:
     #       filename = seq + g + ".txt"
      #      bases = seq.read(filename)hh
       #     total = seq.read(bases, b)

    for g in bases:
        FOLDER = "../sequences/"
        FILENAME = g + ".fa"
        file_contents = Path(FOLDER + FILENAME).read_text()
        header = file_contents.find("\n")
        index0.0 = file_contents[header:]
        c_c = 0
        c_g = 0
        c_a = 0
        c_t = 0
        for b in index:
            if b == "A":
                c_a += 1
            elif b == "G":
                c_g += 1
            elif b == "T":
                c_t += 1
            elif b == "C":
                c_c += 1
        print(g, c_c)
        return

bases = ["ADA"]
lol = seq_count_base(bases)

























