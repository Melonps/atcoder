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
R G B
R G B


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
S = s_list()
T = s_list()


def swap(list, i, j):
    w = list[i]
    list[i] = list[j]
    list[j] = w
    return list


ans_1 = copy.copy(S)
ans_1 = swap(ans_1, 0, 1)
ans_1 = swap(ans_1, 1, 2)

ans_2 = copy.copy(S)
ans_2 = swap(ans_2, 0, 2)
ans_2 = swap(ans_2, 1, 2)
# print(S)
# print(ans_1)
# print(ans_2)

if T == ans_1 or T == ans_2 or T == S:
    print("Yes")
else:
    print("No")
