#from calendar import c
#from collections import Counter, deque, OrderedDict
#from itertools import product
import math
from math import ceil, floor, sqrt, pi, factorial, gcd
##################################
##################################
import sys
import io
#import time

_INPUT = """\
4 2
2 3
0 0
0 1
1 2
2 0


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

N, K = i_map()
A = i_list()

X = [0]*N
Y = [0]*N

m_len = [0]*N

for i in range(0, N):
    X[i], Y[i] = i_map()

for i in range(0, N):
    max_len = INF

    for j in range(0, K):
        nx = A[j] - 1
        max_len = min(max_len, (X[i]-X[nx]) *
                      (X[i]-X[nx]) + (Y[i]-Y[nx])*(Y[i]-Y[nx]))
    m_len[i] = max_len

print(sqrt(max(m_len)))
