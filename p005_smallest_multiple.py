import numpy as np
from math import isqrt, log2


def smallest_multiple(n):
    log_n = log2(n)
    a = np.arange(n + 1)
    a[0] = 1
    for i in range(2, isqrt(n) + 1):
        if a[i] != 1:
            a[i * i::i] = 1
            a[i] = i ** int(log_n / log2(i))
    return a.prod()


def main():
    print(smallest_multiple(20))


if __name__ == '__main__':
    main()
