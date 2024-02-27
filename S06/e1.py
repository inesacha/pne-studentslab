from seq01 import *
s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")

#other ways of doing it
#bases = ['A', 'T', 'C', 'G']
#def __init__(self, strbases):
#self.strbases = ""
#for s in strbases:
#   if s not in Seq.bases:
#       self.strbases = "ERROR"
#       print(ERROR!!)
#       return
#self.strbases = strbases
#print("New sequence created!")

#ok = True
#for s in strbases:
#   if s not in Seq.bases:
#       self.strbases = "ERROR"
#       print(ERROR!!)
#       break
#if ok:
#   self.strbases = strbases
#   print("New sequence created!")