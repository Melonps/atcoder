from calendar import c
from math import ceil, floor, sqrt, pi, factorial, gcd
from collections import Counter, deque, OrderedDict
from itertools import product
import math
import sys
import io
import time
import numpy as np

##################################
##################################

_INPUT = """\
5 5
1
2
3
4
5


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

N, Q = map(int, input().split())
A = [i for i in range(1, N+1)]
support = [i for i in range(0, N)]
# print(A)
# print(support)


def swap(a, b):
    return b, a


for i in range(0, Q):
    q = i_input()
    print('A', A)
    print('support', support)
    target = support[q-1]  # 位置
    if target == N-1:
        A[target], A[target-1] = swap(A[target], A[target-1])
        support[A[target]-1] += 1
        support[A[target-1]-1] -= 1
    else:
        A[target], A[target+1] = swap(A[target], A[target+1])
        support[A[target+1]-1] += 1
        support[A[target]-1] -= 1
