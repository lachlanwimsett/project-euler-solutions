import numpy as np


def main():
    nn: np.ndarray = np.arange(1, 101)
    sum_square = np.square(nn).sum()
    square_sum = nn.sum() ** 2
    diff = square_sum - sum_square
    print(diff)


if __name__ == '__main__':
    main()
