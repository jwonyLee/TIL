# https://www.acmicpc.net/problem/15649
# N과 M (1)
import sys, itertools

m, n = map(int, sys.stdin.readline().split())

# itertools 모듈 사용
for i in list(itertools.permutations(range(1, m+1), n)):
    print(' '.join(map(str, i)))
