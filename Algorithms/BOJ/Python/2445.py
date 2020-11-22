# https://www.acmicpc.net/problem/2445
# 별 찍기 - 8
import sys

n = int(sys.stdin.readline())

for i in range(2*n-1):
    if i < n:
        print("*"*(i+1), end="")
        print(" "*((n-i-1)*2), end="")
        print("*"*(i+1))
    else:
        temp = (abs(i + (n - 1) * -2))+1
        print("*"*((abs(i + (n - 1) * -2))+1), end="")
        print(" "*((n-temp)*2), end="")
        print("*"*((abs(i + (n - 1) * -2))+1))

"""
1 *        *
2 **      **
3 ***    ***
4 ****  ****
5 **********
6 ****  ****
7 ***    ***
8 **      **
9 *        *
"""