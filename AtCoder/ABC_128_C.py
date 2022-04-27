from math import ceil, floor, sqrt, pi, factorial, gcd
from collections import Counter, deque
from itertools import product
import math
import sys
import io
import time


_INPUT = """\
5 2
3 1 2 5
2 2 3
1 0
"""
sys.stdin = io.StringIO(_INPUT)


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

N, M = map(int, input().split())
K = []
S = []
for i in range(M):
    KS = list(map(int, input().split()))
    K.append(KS[0])
    S.append(KS[1:])
p = list(map(int, input().split()))

ans = 0

for pro in product((1, 0), repeat=N):
    L = []
    for a in range(N):
        # proには[4,5]とか[1,2,3,4]とかが入ってる
        if pro[a] == 1:
            L.append(a+1)
    klight = 1
    print(L)
    for i in range(M):
        score = 0
        light = 0
        for j in range(K[i]):
            # print(S[i][j])
            if S[i][j] in L:
                light += 1
        # 光るライトの数
        # print(light)
        if light % 2 == p[i]:
            score += 1
            # print(light)

        klight *= score
        print(klight)
    ans += klight

    # print(ans)
print(ans)
