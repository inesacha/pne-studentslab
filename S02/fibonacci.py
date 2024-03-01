x1 = 0
print(x1)
x2 = 1
print(x2)
for i in range(3, 12):
    x3 = x1 + x2
    print(x3)
    x1 = x2
    x2 = x3
    i += 1


