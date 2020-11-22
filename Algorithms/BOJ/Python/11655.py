# https://www.acmicpc.net/problem/11655
# ROT13
import sys

ROT = 13
word = sys.stdin.readline()

for w in word:
    if w.isspace() or w.isdigit():
        print(w, end="")
    elif w.islower(): # 97 ~ 122
        temp = ord(w) + ROT
        if temp > 122:
            temp = 96 + temp - 122
        print(chr(temp), end="")
    elif w.isupper(): # 65 ~ 90
        temp = ord(w) + ROT
        if temp > 90:
            temp = 64 + temp - 90
        print(chr(temp), end="")
print()