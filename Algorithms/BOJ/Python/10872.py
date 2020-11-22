import sys

n = int(sys.stdin.readline())

if n < 1:
    result = 1
else:
    result = 1
    for i in range(1, n+1):
        result *= i

print(result)