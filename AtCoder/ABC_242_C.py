from calendar import c
from math import ceil, floor, sqrt, pi, factorial, gcd
from collections import Counter, deque, OrderedDict
from itertools import product
import math
import sys
import io
import time

##################################
##################################

_INPUT = """\
4



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

# 二次配列系
# l = [[0 for i in range(3)] for j in range(2)]
# [[0, 0, 0], [0, 0, 0]]
# l[2][3] = 1


def row_sum(list): return [sum(row) for row in dp]


# start = time.time()
# elapsed_time = time.time() - start
# print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

# Shift+alt+fでコード成形

INF = float('inf')
MOD = 10 ** 9 + 7
# start = time.time()


##################################
##################################

N = int(input())
M = 998244353

X = [1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(N-1):
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    x[0] = (X[0] + X[1]) % M
    x[1] = (X[0] + X[1] + X[2]) % M
    x[2] = (X[1] + X[2] + X[3]) % M
    x[3] = (X[2] + X[3] + X[4]) % M
    x[4] = (X[3] + X[4] + X[5]) % M
    x[5] = (X[4] + X[5] + X[6]) % M
    x[6] = (X[5] + X[6] + X[7]) % M
    x[7] = (X[6] + X[7] + X[8]) % M
    x[8] = (X[7] + X[8]) % M
    X = x

print(sum(X) % M)
