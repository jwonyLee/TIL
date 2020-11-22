# https://www.acmicpc.net/problem/1267
# 핸드폰 요금
import sys

n = int(sys.stdin.readline())
calls = list(map(int, sys.stdin.readline().split()))

y_prices = []
m_prices = []

for c in calls:
    y_price = 0
    m_price = 0
    # 영식 요금제 요금 구하기
    if (c + 1) - ((c // 30) * 30) == 0:
        y_price = (c // 30) * 10
    else:
        y_price = ((c // 30) + 1 ) * 10
    # 민식 요금제 요금 구하기
    if (c + 1) - ((c // 60) * 60) == 0:
        m_price = (c // 60) * 15
    else:
        m_price = ((c // 60) + 1 ) * 15
    
    y_prices.append(y_price)
    m_prices.append(m_price)

if sum(y_prices) > sum(m_prices):
    print("M", sum(m_prices))
elif sum(y_prices) < sum(m_prices):
    print("Y", sum(y_prices))
else:
    print("Y M", sum(y_prices))