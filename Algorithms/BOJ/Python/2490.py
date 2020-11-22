import sys

for i in range(3):
    n = sys.stdin.readline().split()
    result = n.count('0')
    if result == 1:
        print('A')
    elif result == 2:
        print('B')
    elif result == 3:
        print('C')
    elif result == 4:
        print('D')
    else:
        print('E')