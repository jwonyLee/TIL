import sys
n = int(sys.stdin.readline())
a = []
for i in range(n):
    b = sys.stdin.readline().split()
    b[0] = int(b[0])
    b.append(i)
    a.append(b)

a.sort(key=lambda x: (x[0], x[2]))

for s in a:
    print(s[0], s[1])