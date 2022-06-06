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
2 3
--o
o--

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

H, W = i_map()
S = []
cnt = 0
x_diff = []
y_diff = []

for i in range(H):
    s = s_input()
    S.append(s)
    for j in range(W):
        if s[j] == 'o':
            x_diff.append(j)
            y_diff.append(i)

# print(S)
# print(x_diff)
# print(y_diff)
print(abs(x_diff[1]-x_diff[0])+abs(y_diff[1]-y_diff[0]))
