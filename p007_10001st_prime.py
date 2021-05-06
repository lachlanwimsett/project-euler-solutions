from math import isqrt
from itertools import islice


def sieve(n):
    a = 0
    i = 2
    for i in range(2, isqrt(n) + 1):
        a >>= 1
        if a & 1 == 0:
            yield i
            i2 = i * i
            b = 1 << (i2 - i)
            for _ in range(i2, n + 1, i):
                a |= b
                b <<= i
    for i in range(i + 1, n + 1):
        a >>= 1
        if a & 1 == 0:
            yield i


def main():
    print(next(islice(sieve(105_000), 10001 - 1, 10001)))


if __name__ == '__main__':
    main()
