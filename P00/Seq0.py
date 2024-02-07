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

def seq_len():
    gene_list = ["U5", "ADA", "FRAT1", "FXN"]
    for i in gene_list:
        i += ".fa"

