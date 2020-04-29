import sys

while True:
    triangle = list(map(int, sys.stdin.readline().split()))
    if triangle.count(0) == 3:
        break
    triangle.sort()

    big = triangle[2] ** 2
    temp = triangle[0] ** 2 + triangle[1] ** 2
    if big == temp:
        print("right")
    else:
        print("wrong")