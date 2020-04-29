import sys


money = 1000 - int(sys.stdin.readline())

item = 0

if int(money / 500) > 0:
    c = int(money / 500)
    money -= c * 500
    item += c
if int(money / 100) > 0:
    c = int(money / 100)
    money -= c * 100
    item += c
if int(money / 50) > 0:
    c = int(money / 50)
    money -= c * 50
    item += c
if int(money / 10) > 0:
    c = int(money / 10)
    money -= c * 10
    item += c
if int(money / 5) > 0:
    c = int(money / 5)
    money -= c * 5
    item += c
if int(money / 1) > 0:
    c = int(money / 1)
    money -= c * 1
    item += c

print(item)