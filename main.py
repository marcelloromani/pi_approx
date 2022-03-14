#!/usr/bin/env python3
from random import random


def approx_pi(cycle_count: int) -> float:
    x = [(random(), random()) for i in range(cycle_count)]
    z = [y[0] ** 2 + y[1] ** 2 < 1 for y in x]
    pi = 4.0 * sum(z) / len(z)
    return pi


def main():
    tests = [
        100,
        1000,
        10000,
        100000,
        1000000,
    ]
    for t in tests:
        pi = approx_pi(t)
        print(f"{t:10}  ==>  {pi}")


if __name__ == "__main__":
    main()
