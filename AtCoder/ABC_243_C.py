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
10
1 3
1 4
0 0
0 2
0 4
3 1
2 4
4 2
4 4
3 3
RLRRRLRLRR

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
def YES():
    print("Yes")
    exit(0)


N = i_input()

XY = ()
for i in range(N):
    X, Y = i_map()
    XY += ((X, Y),)

# print(XY)
RL = s_input()

Y_R = {}
Y_L = {}

for i in range(0, N):
    x = XY[i][0]
    y = XY[i][1]
    if RL[i] == 'R':
        if y in Y_L and x < Y_L[y]:
            YES()
    else:
        if y in Y_R and x > Y_R[y]:
            YES()

    if RL[i] == 'R':
        if (y in Y_R):
            Y_R[y] = min(x, Y_R[y])
        else:
            Y_R[y] = x
    else:
        if (y in Y_L):
            Y_L[y] = max(x, Y_R[y])
        else:
            Y_L[y] = x
# print(Y_R)
# print(Y_L)
print("No")
