"""Write a program to print a series -
(1*1^1)/1! + (2*2^2)/2! + ....... + (n*n^n)/n!"""


def factorial(c):
    if c == 1:
        return 1
    else:
        return c * factorial(c - 1)


def power(c, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / (c * power(c, b + 1))
    else:
        return c * power(c, b - 1)


def add(c):
    d = 0
    if c == 1:
        return 1
    else:
        d += (c * power(c, c) / factorial(c))
        return d + add(c-1)


n = int(input("Enter no"))
a = add(n)
print("Sum of series is ", a)
