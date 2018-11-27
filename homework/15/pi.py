from random import uniform

def calc_PI():
    n_points = 1000000
    hits = 0

    for i in range(1, n_points):
        x, y = uniform(0.0, 1.0), uniform(0.0, 1.0)

        if (x**2 + y**2) <= 1.0:
            hits += 1

    print("Calc: PI result", 4.0 * float(hits) / n_points)

if __name__ == "__main__":
    calc_PI()