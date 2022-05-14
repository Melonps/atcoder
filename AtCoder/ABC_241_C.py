from calendar import c
from math import ceil, floor, sqrt, pi, factorial, gcd
from collections import Counter, deque, OrderedDict
from itertools import product
import math
import sys
import io
import time
import copy

##################################
##################################

_INPUT = """\
8
........
........
.#.##.#.
........
........
........
........
........

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
# l[j][i] = 1


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

N = i_input()
S = [input()for _ in range(N)]
Dx = [1, 0, 1, 1]
Dy = [0, 1, 1, -1]


def calc(x, y, dx, dy):
    count = 0
    for i in range(6):
        if not (0 <= min(x, y) and max(x, y) < N):
            return 0
        if S[x][y] == '#':
            count += 1
        x += dx
        y += dy
    return count >= 4


print(S)

for i in range(0, N):
    for j in range(0, N):
        for dx, dy in zip(Dx, Dy):
            if calc(i, j, dx, dy):
                print("Yes")
                exit()
print("No")
