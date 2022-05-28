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
1 2 2 3 3 4 4 5 5 5 6 7 8 9


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

h = i_list()
set_h = set(h)

print("もとの配列hは", h)
print("setオブジェクトにいれると", set_h)

# 空のsetオブジェクト
s = set()
print(s)
print(type(s))

# listのようにsetにあるかどうか判定できる
if 2 in set_h:
    print('2はsetにあります')

# addで新たな要素を追加
set_h.add(11)
print("追加後", set_h)

# 削除
set_h.discard(1)
print("削除後", set_h)
