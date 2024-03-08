from pathlib import Path

class Seq:
    bases = ['A', 'T', 'C', 'G']

    def __init__(self, strbases=None):
        if strbases is None:
            self.strbases = "NULL"
            print("NULL sequence created")
        else:
            for s in strbases:
               if s not in Seq.bases:
                   self.strbases = "ERROR"
                   print("INVALID sequence!")
                   return
            self.strbases = strbases
            print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        return len(self.strbases)

    def count_base(self, base):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            return self.strbases.count(base)

    def count(self):
        d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        if self.strbases != "NULL" or self.strbases != "ERROR":
            for g in self.strbases:
                if g == "A":
                    d['A'] += 1
                elif g == "T":
                    d['T'] += 1
                elif g == "C":
                    d['C'] += 1
                elif g == "G":
                    d['G'] += 1
        return d

    def reverse(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return self.strbases
        else:
            reverse_fragment = ""
            for i in reversed(range(len(self.strbases))):
                reverse_fragment += self.strbases[i]
            return reverse_fragment

    def complement(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return self.strbases
        else:
            complement_fragment = ""
            for g in self.strbases:
                if g == "A":
                    complement_fragment += "T"
                elif g == "T":
                    complement_fragment += "A"
                elif g == "C":
                    complement_fragment += "G"
                elif g == "G":
                    complement_fragment += "C"
            return complement_fragment

    def read_fasta(self, filename):
        folder = "../sequences/"
        filename = filename + ".txt"
        file_contents = Path(folder + filename).read_text()
        header = file_contents.find("\n")
        body = file_contents[header:]
        list_contents = body.replace("\n", "")
        self.strbases = list_contents
        return self.strbases

    def processing_the_genes(self, filename):
        gene = self.read_fasta(filename)
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
        return answer




class Gene(Seq):
    def __init__(self, strbases, name=""):
        super().__init__(strbases)
        self.name = name
        print("New gene created")

    def __str__(self):
        return self.name + "-" + self.strbases