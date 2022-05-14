from calendar import c
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
7 8
2 2
4 5
########
#......#
#.######
#..#...#
#..##..#
##.....#
########


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
R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sy, sx, gy, gx = sy-1, sx-1, gy-1, gx-1
c = [[c for c in input()] for _ in range(R)]
visited = [[-1]*C for _ in range(R)]

print(c)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(sy, sx, gy, gx, c, visited):
    visited[sy][sx] = 0
    Q = deque([])
    Q.append([sy, sx])
    while Q:
        y, x = Q.popleft()

        if[y, x] == [gy, gx]:
            return visited[y][x]

        for i, j in zip(dy, dx):
            if c[y+i][x+j] == '.' and visited[y+i][x+j] == -1:
                # 探索可能かつ未探索の場合
                visited[y+i][x+j] = visited[y][x]+1
                Q.append([y+i, x+j])


print(bfs(sy, sx, gy, gx, c, visited))
