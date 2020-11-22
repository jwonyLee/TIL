import sys

h, m = map(int, sys.stdin.readline().strip().split())

# H시가 0이 면서 M분이 45분보다 작을 때
if h == 0 and m < 45:
    h = 23
    m = 60 - (45 - m)
    print(h, m)

# M분이 45분보다 크거나 같을 때
elif m >= 45:
    m -= 45
    print(h, m)

# M분이 45분보다 작을 때
elif m < 45:
    h -= 1
    m = 60 - (45 - m)
    print(h, m)