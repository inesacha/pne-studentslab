def fiboN (n):
    x1 = 0
    x2 = 1
    while n > 0:
        x3 = x1 + x2
        x1 = x2
        x2 = x3
        n -= 1
    return x1
print("5th Fibonacci term:", fiboN(5), "\n10th Fibonacci term:", fiboN(10), "\n15th Fibonacci term:", fiboN(15))