# https://www.acmicpc.net/problem/5430
# AC
# 참고: https://www.acmicpc.net/board/view/25456
import sys, collections
t = int(sys.stdin.readline())
for _ in range(t):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    x = sys.stdin.readline()[1:-2].split(",")
    flag = False
    error = False
    h = 0 # head
    e = n # tail
    for s in p:
        if s in "R":
            flag = not flag
        elif s in "D":
            if h != e:
                if flag:
                    # x.pop()
                    e -= 1
                else:
                    # x.popleft()
                    h += 1
            else:
                error = True
    if not error:
        if flag:
            print("[{}]".format(','.join(reversed(x[h:e]))))
        else:
            print("[{}]".format(','.join(x[h:e])))
    else:
        print("error")