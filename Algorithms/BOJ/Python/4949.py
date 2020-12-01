# https://www.acmicpc.net/problem/4949
# 균형잡힌 세상
import sys
word = sys.stdin.readline().rstrip('.')
while len(word) > 2:
    flag = True
    s = []
    for c in word:
        if c in '([':
            s.append(c)
        elif c in ')':
            if s:
                if s.pop() != '(':
                    flag = False
            else:
                flag = False
        elif c in ']':
            if s:
                if s.pop() != '[':
                    flag = False
            else:
                flag = False

    if s:
        print("no")
    elif flag:
        print("yes")
    else:
        print("no")
    word = sys.stdin.readline().rstrip('.')