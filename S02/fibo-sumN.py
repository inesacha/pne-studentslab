def fiboN (n):
    x1 = 0
    x2 = 1
    while n > 0:
        x3 = x1 + x2
        x1 = x2
        x2 = x3
        n -= 1
    return x1


def fibosum(n):
    res = 0
    for i in range(1, n + 1):
        res += fiboN(i)
    return res


print("Sum of the first 5 terms of the Fibonacci series: ", fibosum(5))
print("Sum of the first 10 terms of the Fibonacci series: ", fibosum(10))
