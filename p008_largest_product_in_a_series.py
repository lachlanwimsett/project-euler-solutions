from numpy import genfromtxt, log2, exp2, ones, convolve


def main():
    series = genfromtxt('p008_series.txt', delimiter=1)
    k = ones(13, dtype=int)
    max_product = round(max(exp2(convolve(log2(series), k, 'valid'))))
    print(max_product)


if __name__ == '__main__':
    main()
