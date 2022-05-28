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
4 12
3 3 3 3


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

N, W = i_map()
A = i_list()
A.insert(0, 0)
A.insert(0, 0)

good_n = set()

for i in range(0, len(A)-2):
    for j in range(i+1, len(A)-1):
        for k in range(j+1, len(A)):
            sum = A[i] + A[j] + A[k]
            good_n.add(sum)

# print(good_n)
cnt = 0
good_n = list(good_n)
for i in range(len(good_n)):
    if good_n[i] <= W:
        cnt += 1

print(cnt)
