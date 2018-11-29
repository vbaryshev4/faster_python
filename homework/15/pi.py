from random import random
from multiprocessing import Pool


def count_hits(n_points):
    result = 0
    for i in range(n_points):
        x, y = random(), random()
        if (x ** 2 + y ** 2) <= 1:
            result += 1
    return result

def calc_PI(accuracy=1):
    n_points = (10**2)**accuracy

    with Pool(4) as p:
        hits = (sum(p.map(count_hits, [int(n_points / 4)] * 4)))
    print("Calc: PI result", round(((4 * hits) / n_points), accuracy))


if __name__ == "__main__":
    calc_PI(4)