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
4 2
abi
aef
bc
acg

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
def judge(text, K):
    text_n = ''.join(OrderedDict.fromkeys(text))
    cnt = 0
    for i in text_n:
        if text.count(i) == K:
            cnt += 1
    return cnt


N, K = i_map()
cnt_max = 0

S = ()
for i in range(0, N):
    S = S + (s_input(),)

# print(S)
S_n = ''.join(OrderedDict.fromkeys(S))
# print(S_n)

for bits in product([0, 1], repeat=N):
    l = ''
    #print("bits: ", bits)
    a = [x for bit, x in zip(bits, S) if bit == 1]
    text = "".join(map(str, a))
    # print(text)
    cnt = (judge(text, K))
    cnt_max = max(cnt, cnt_max)

print(cnt_max)
