import sys

buger = []
drink = []

for i in range(3):
    buger.append(int(sys.stdin.readline()))
for i in range(2):
    drink.append(int(sys.stdin.readline()))

print(min(buger) + min(drink) - 50)