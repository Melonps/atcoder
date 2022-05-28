from math import ceil, floor, sqrt, pi, factorial, gcd
from collections import Counter, deque, OrderedDict
from itertools import product
import math
import sys
import io
import time

from numpy import s_

##################################
##################################

_INPUT = """\
2
tanaka taro
tanaka taro


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
S = [0]*N
T = [0]*N
A = [0]*N

for i in range(0, N):
    S[i], T[i] = s_map()

for i in range(N):
    set_s = set()
    set_t = set()
    for j in range(N):
        if i == j:
            continue
        else:
            set_s.add(S[j])
            set_t.add(T[j])
    #print(S[i], T[i])
    # print(set_s)
    # print(set_t)
    if not S[i] in set_s and not S[i] in set_t:
        A[i] += 1
    if not T[i] in set_s and not T[i] in set_t:
        A[i] += 1


# print(A)
if 0 in A:
    print('No')
else:
    print('Yes')
