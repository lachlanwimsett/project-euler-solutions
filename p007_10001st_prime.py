from math import isqrt, log, ceil


def prime(n):
    limit = ceil(n * log(n) + n * log(log(n)))
    a = 0
    k = 0
    i = 2
    for i in range(2, isqrt(limit) + 1):
        a >>= 1
        if a & 1 == 0:
            k += 1
            b = 1 << (i * i - i)
            for _ in range(i * i, limit + 1, i):
                a |= b
                b <<= i
    for i in range(i + 1, limit + 1):
        a >>= 1
        if a & 1 == 0:
            k += 1
            if k == n:
                return i


def main():
    print(prime(10001))


if __name__ == '__main__':
    main()
