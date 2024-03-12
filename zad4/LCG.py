import random


def lcg(x, a, c, m):
    while True:
        x = (a * x + c) % m
        yield x


def random_uniform_sample(n, seed=0):
    seed, a, c, m = 42, 1103515245, 12345, 2 ** 31 - 1
    bsdrand = lcg(seed, a, c, m)
    sample = []

    for i in range(n):
        sample.append(next(bsdrand)%2)

    return sample

if (__name__ == "__main__"):
    f = open("bits.txt", "w")
    #f.write(f"{''.join([str(i) for i in random_uniform_sample(1000000)])}")
    f.write(f"{''.join([str(i) for i in [random.randint(0, 1) for _ in range(1000000)]])}")
    f.close()
