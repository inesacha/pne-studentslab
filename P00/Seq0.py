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

def seq_count_base (seq, bases):
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

    print(f"Gene", seq, ":", "\n   A:", answer["A"], "\n   C:", answer["C"], "\n   G:", answer["G"], "\n   T:", answer["T"])



























