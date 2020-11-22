# https://www.acmicpc.net/submit/6996
# 애너그램

import sys
n = int(sys.stdin.readline())
for _ in range(n):
    a, b = sys.stdin.readline().strip().split()
    if sorted(a) == sorted(b):
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")