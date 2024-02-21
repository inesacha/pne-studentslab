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


def seq_count_base(seq, bases):
    FOLDER = "../sequences/"
    FILENAME = seq + ".fa"
    file_contents = Path(FOLDER + FILENAME).read_text()
    header = file_contents.find("\n")
    gene = file_contents[header:]
    answer = {}
    for g in gene:
        for b in bases:
            if g == b:
                if b not in answer.keys():
                    answer[b] = 1
                else:
                    answer[b] += 1
    print("Gene", seq, ":", "\n   A:", answer["A"], "\n   C:", answer["C"], "\n   T:", answer["T"], "\n   G:", answer["G"])

def seq_count(seq):
    FOLDER = "../sequences/"
    FILENAME = seq + ".fa"
    file_contents = Path(FOLDER + FILENAME).read_text()
    header = file_contents.find("\n")
    gene = file_contents[header:]
    d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for g in gene:
        if g == "A":
            d['A'] += 1
        elif g == "T":
            d['T'] += 1
        elif g == "C":
            d['C'] += 1
        elif g == "G":
            d['G'] += 1
    print(f"Gene {seq}: {d}")


def seq_reverse(seq, n):
    FOLDER = "../sequences/"
    FILENAME = seq + ".fa"
    file_contents = Path(FOLDER + FILENAME).read_text()
    header = file_contents.find("\n")
    gene = file_contents[header + 1:]
    new_fragment = gene[:n]
    reverse_fragment = ""
    for i in reversed(range(20)):
        reverse_fragment += new_fragment[i]
    print(f"Gene {seq}\nFragment: {new_fragment}\nReverse: {reverse_fragment}")


def seq_complement(seq):
    FOLDER = "../sequences/"
    FILENAME = seq + ".fa"
    file_contents = Path(FOLDER + FILENAME).read_text()
    header = file_contents.find("\n")
    gene = file_contents[header + 1:]
    new_fragment = gene[:20]
    complement_fragment = ""
    for g in new_fragment:
        if g == "A":
            complement_fragment += "T"
        elif g == "T":
            complement_fragment += "A"
        elif g == "C":
            complement_fragment += "G"
        elif g == "G":
            complement_fragment += "C"
    print(f"Gene {seq}\nFrag: {new_fragment}\nComp: {complement_fragment}")


def processing_the_genes(seq):
    FOLDER = "../sequences/"
    FILENAME = seq + ".fa"
    file_contents = Path(FOLDER + FILENAME).read_text()
    header = file_contents.find("\n")
    gene = file_contents[header:]
    d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for g in gene:
        if g == "A":
            d['A'] += 1
        elif g == "T":
            d['T'] += 1
        elif g == "C":
            d['C'] += 1
        elif g == "G":
            d['G'] += 1

    biggest_value = 0
    answer = ""
    for keys in d:
        if biggest_value < d[keys]:
            biggest_value = d[keys]
            answer = keys

    print(f"Gene {seq}: Most frequent base: {answer}")























