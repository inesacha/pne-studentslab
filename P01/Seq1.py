class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        count = 0
        for s in strbases:
            if s == "A":
                count += 1
            elif s == "C":
                count += 1
            elif s == "G":
                count += 1
            elif s == "T":
                count += 1
        if count != len(strbases):
            self.strbases = "ERROR"
            print("ERROR!!")
        else:
            self.strbases = strbases
            print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)


class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inherit
       the methods from the Seq class
    """
    def __init__(self, strbases, name=""):

        # -- Call first the Seq initializer and then the
        # -- Gene init method
        super().__init__(strbases)
        self.name = name
        print("New gene created")

    def __str__(self):
        """Print the Gene name along with the sequence"""
        return self.name + "-" + self.strbases