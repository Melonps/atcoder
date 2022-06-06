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
4

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

N = i_input()

heihou = []


def prime_fact(N):
    i = 2
    l = []
    ex_l = []
    while i * i <= N:
        #print(N, i)
        if(N % i == 0):
            ex = 0
            while N % i == 0:
                ex += 1
                N = N / i
            l.append(i)
            ex_l.append(ex)
        i += 1
    if N != 1:
        l.append(N)
        ex_l.append(1)
    # for i in range(0, len(l)):
        #print(i, "番目に", l[i], "があり指数は", ex_l[i])
    return ex_l


print(prime_fact(36))


def count_heihou(ex_l):
    for i in range(0, len(ex_l)):
        ex_l[i] += 1
    prod = 1
    for i in ex_l:
        prod *= i
    print(prod)
    return prod + 1


heihou = []
cnt = 0
i = 1
while i*i <= N:
    heihou.append(i*i)
    i += 1

print(heihou)
for i in heihou:
    cnt += count_heihou(prime_fact(i))
print(cnt)
