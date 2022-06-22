from calendar import c
from math import ceil, floor, prod, sqrt, pi, factorial, gcd
from collections import Counter, deque, OrderedDict
from itertools import product
import math
import sys
import io
import time

##################################
##################################

_INPUT = """\
abaababaab


"""
sys.stdin = io.StringIO(_INPUT)

##################################
##################################


def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)  # 最小公倍数

# l = [[0 for i in range(3)] for j in range(2)]
# [[0, 0, 0], [0, 0, 0]]
# l[2][3] = 1


# start = time.time()
# elapsed_time = time.time() - start
# print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

# Shift+alt+fでコード成形


INF = float('inf')
MOD = 10 ** 9 + 7
# start = time.time()


##################################
##################################

X, A, D, N = i_map()

max_S = max(D * (N - 1) + A, A)
min_S = min(D * (N - 1) + A, A)

if X <= max_S and X >= min_S:
    target = X - A
    if D == 0:
        print(abs(A - X))
    else:
        print(target % D)
else:
    diff_min = abs(min_S - X)
    diff_max = abs(X - max_S)
    print(min(diff_max, diff_min))

print(min_S, max_S)
