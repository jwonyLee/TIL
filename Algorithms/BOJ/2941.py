# https://www.acmicpc.net/problem/2941
# 크로아티아 알파벳
# c=, c-, dz=, d-, lj, nj, s=, z=

import sys

text = sys.stdin.readline().strip()
i = 0
num = 0

if len(text) < 2:
    print(1)
else:
    while i < len(text):
        if i + 1 >= len(text):
            num += 1
            break
        if text[i] == "c" and text[i+1] == "=" or text[i+1] == "-":
            num += 1
            i += 2
            continue
        if text[i] == "d":
            if text[i+1] == "-":
                num += 1
                i += 2
                continue
            elif i+2 < len(text) and (text[i+1] == "z" and text[i+2] == "="):
                num += 1
                i += 3
                continue
        if text[i] == "l" and text[i+1] == "j":
            num += 1
            i += 2
            continue
        if text[i] == "n" and text[i+1] == "j":
            num += 1
            i += 2
            continue
        if text[i] == "s" and text[i+1] == "=":
            num += 1
            i += 2
            continue
        if text[i] == "z" and text[i+1] == "=":
            num += 1
            i += 2
            continue
        i += 1
        num += 1

    print(num)