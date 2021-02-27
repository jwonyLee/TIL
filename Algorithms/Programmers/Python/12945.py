# https://programmers.co.kr/learn/courses/30/lessons/12945
# 피보나치 수
def solution(n):
    f = [0] * 100001
    f[1] = 1
    f[2] = 1
    for i in range(3, 100001):
        f[i] = f[i-1] + f[i-2]
    return f[n] % 1234567