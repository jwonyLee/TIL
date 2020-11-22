import sys

price = int(sys.stdin.readline())
temp = 0

for i in range(9):
    temp += int(sys.stdin.readline())

print(price - temp)

