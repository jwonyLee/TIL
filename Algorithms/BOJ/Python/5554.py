import sys

time = 0

for i in range(4):
    time += int(sys.stdin.readline())

m = int(time / 60)
time -= m * 60
print(m)
print(time)