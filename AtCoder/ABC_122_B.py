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
HATAGAYA


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
S = s_input()
N = len(S)

max_l = 0

for i in range(N):
    if S[i] == 'A' or S[i] == 'C' or S[i] == 'G' or S[i] == 'T':
        go = 1
        cnt = 1
        while (go):
            if i == N-1:
                go = 0
                break
            i += 1
            if S[i] == 'A' or S[i] == 'C' or S[i] == 'G' or S[i] == 'T':
                cnt += 1
            else:
                go = 0

        max_l = max(cnt, max_l)


print(max_l)
