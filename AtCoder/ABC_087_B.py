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
2
2
2
100


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

A = i_input()
B = i_input()
C = i_input()
X = i_input()

cnt = 0

for i in range(0, A+1):
    for j in range(0, B+1):
        for k in range(0, C+1):
            if(i*500 + j*100 + k*50 == X):
                cnt += 1
                #print(i, j, k)

print(cnt)
