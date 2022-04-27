from math import ceil, floor, sqrt, pi, factorial, gcd
from collections import Counter, deque
import math
import sys
import io
_INPUT = """\
10 20 30 40 50 60 70 80 90
40
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

# Shift+alt+fでコード成形！


INF = float('inf')
MOD = 10 ** 9 + 7

sys.stdin = io.StringIO(_INPUT)

A = i_list()
target = i_input()


def binary_search(A, target):
    left = 0
    right = len(A) - 1

    while left <= right:
        mid = (right + left) // 2
        if A[mid] == target:
            return mid
        elif A[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


print(binary_search(A, target))
