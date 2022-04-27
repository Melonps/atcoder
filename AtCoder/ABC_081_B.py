from math import ceil, floor, sqrt, pi, factorial, gcd
from collections import Counter, deque
from itertools import product
import math
import sys
import io
import time

##################################
##################################

_INPUT = """\
6
382253568 723152896 37802240 379425024 404894720 471526144

"""
sys.stdin = io.StringIO(_INPUT)

##################################
##################################


def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def lcm(a, b): return a * b // gcd(a, b)  # 最小公倍数

#l = [[0 for i in range(3)] for j in range(2)]
#[[0, 0, 0], [0, 0, 0]]
#l[2][3] = 1


#start = time.time()
#elapsed_time = time.time() - start
#print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

# Shift+alt+fでコード成形


INF = float('inf')
MOD = 10 ** 9 + 7
#start = time.time()


##################################
##################################

N = i_input()
A = i_list()

cnt_min = 100

for a in A:
    cnt = 0
    while a % 2 == 0:
        cnt += 1
        a = a // 2

    if cnt < cnt_min:
        cnt_min = cnt


print(cnt_min)
