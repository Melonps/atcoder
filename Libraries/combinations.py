from itertools import combinations
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
7 251
202 20 5 1 4 2 100


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


def at_most_three_judge_faster():
    N, W = map(int, input().split())
    A = list(map(int, input().split())) + [0, 0]  # これがポイント、ちょうど0が含まれるようにする
    flag = [False] * (W + 1)

    for x, y, z in combinations(A, 3):  # Aのなかから3つ選んでくれる
        w = x+y+z
        print(x, y, z)
        if w <= W:
            flag[w] = True

    return flag.count(True)


if __name__ == "__main__":
    print(at_most_three_judge_faster())
