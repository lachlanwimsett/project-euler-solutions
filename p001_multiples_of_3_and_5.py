def triangular(n):
    return n * (n + 1) // 2


def main():
    mul_3 = 3 * triangular(999 // 3)
    mul_5 = 5 * triangular(999 // 5)
    mul_15 = 15 * triangular(999 // 15)
    mul_3_and_5 = mul_3 + mul_5 - mul_15
    print(mul_3_and_5)


if __name__ == '__main__':
    main()
