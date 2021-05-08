from math import isqrt, log, ceil


def bit_count(int_type):
    count = 0
    while int_type:
        int_type &= int_type - 1
        count += 1
    return count


def prime(n):
    limit = ceil(n * log(n) + n * log(log(n)))
    a = 0
    k = 0
    p = 2
    for i in range(2, isqrt(limit) + 1):
        a >>= 1
        if a & 1 == 0:
            p = i
            k += 1
            b = 1 << (i * i - i)
            for _ in range(i * i, limit + 1, i):
                a |= b
                b <<= i
    a ^= (1 << a.bit_length()) - 1
    primes = bit_count(a) + k

    for _ in range(primes, n, -1):
        a &= (1 << a.bit_length() - 1) - 1
    return a.bit_length() + p


def main():
    print(prime(10001))


if __name__ == '__main__':
    main()
