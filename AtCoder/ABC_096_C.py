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
5 5
#.#.#
.#.#.
#.#.#
.#.#.
#.#.#



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
dir_x = [0, 1]
dir_y = [1, 0]
map = []
flag = 1

for i in range(H):
    map.append(s_input())

for i in range(H):
    for j in range(W):
        if i + 1 == H or j + 1 == W or j - 1 < 0 or i - 1 < 0:
            continue
        else:
            if map[i + 1][j] == '.' and map[i][j + 1] == '.' and map[i][j - 1] == '.' and map[i - 1][j] == '.' and map[i][j] == '#':
                #print(i, j)
                flag = 0


if flag:
    print('Yes')
else:
    print('No')
