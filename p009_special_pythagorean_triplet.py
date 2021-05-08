from itertools import count


def main():
    for m in count(2):
        for n in range(1, m):
            k, r = divmod(m * m + m * n, 500)
            if r == 0:
                a = k * (m * m - n * n)
                b = k * 2 * m * n
                c = k * (m * m + n * n)
                assert a ** 2 + b ** 2 == c ** 2
                assert a + b + c == 1000
                print(a * b * c)
                return


if __name__ == '__main__':
    main()
