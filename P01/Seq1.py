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


class Gene(Seq):
    def __init__(self, strbases, name=""):
        super().__init__(strbases)
        self.name = name
        print("New gene created")

    def __str__(self):
        return self.name + "-" + self.strbases