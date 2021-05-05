def is_palindrome(n):
    r, m, = 0, n
    while m > 0:
        m, d = divmod(m, 10)
        r *= 10
        r += d
    return r == n


def main():
    products = {a * b for a in range(101, 1000) for b in range(a, 1000)}
    max_palindrome = max(p for p in products if is_palindrome(p))
    print(max_palindrome)


if __name__ == '__main__':
    main()
