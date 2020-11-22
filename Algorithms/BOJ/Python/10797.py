import sys

day = int(sys.stdin.readline())
car = list(map(int, sys.stdin.readline().split()))

print(car.count(day))