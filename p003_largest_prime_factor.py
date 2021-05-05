from math import gcd
from heapq import heappop, heappush


def pollard_rho(n):
    def g(x):
        return (pow(x, 2, n) + 1) % n

    x, y, d = 2, 2, 1
    while d == 1:
        x, y = g(x), g(g(y))
        d = gcd(abs(x - y), n)
    return d if d != n else None


def largest_prime_factor(n):
    queue = [-n]
    while a := pollard_rho(n := -heappop(queue)):
        b = n // a
        heappush(queue, -a)
        heappush(queue, -b)
    return n


def main():
    n = 600851475143
    lpf = largest_prime_factor(n)
    print(lpf)


if __name__ == '__main__':
    main()
