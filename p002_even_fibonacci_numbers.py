def main():
    s = 0
    a, b = 0, 1
    for i in range(34):
        if i % 3 == 0:
            s += a
        a, b = b, a + b
    print(s)


if __name__ == '__main__':
    main()
