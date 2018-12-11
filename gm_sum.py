#!/usr/bin/env python
import sys
import math


def gm_sum(initial_val, ratio, N):
    val = float(initial_val)
    r = float(ratio)
    n = float(N)
    return val * (1 - math.pow(r, n)) / (1 - r)


if __name__ == '__main__':
    print(gm_sum(sys.argv[1], sys.argv[2], sys.argv[3]))
