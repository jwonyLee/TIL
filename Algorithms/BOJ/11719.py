# https://www.acmicpc.net/problem/11719
# 그대로 출력하기 2

while True:
    try: 
        text = input()
        print(text)
    except EOFError:
        break