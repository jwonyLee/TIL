import sys

result = 0

for i in range(5):
    n = int(sys.stdin.readline())
    if n < 40:
        result += 40
    else:
        result += n

print(int(result/5))

