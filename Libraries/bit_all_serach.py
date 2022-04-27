from math import ceil, floor, sqrt, pi, factorial, gcd
from collections import Counter, deque
import math
import sys
import io
import time

_INPUT = """\
300 3
みかん 100
りんご 200
ぶどう 300
"""


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

sys.stdin = io.StringIO(_INPUT)
##################################
##################################

target, N = i_map()
item = tuple()
for i in range(0, N):
    name, money = s_map()
    item = item + ((name, int(money)),)

for i in range(2 ** N):
    bag = []
    sum = 0
    #print("pattern {}: ".format(i), end="")
    for j in range(N):
        if ((i >> j) & 1):
            bag.append(item[j][0])
            sum += item[j][1]
    if(sum <= target):
        print(sum, bag)

#elapsed_time = time.time() - start
#print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
