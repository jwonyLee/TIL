# https://programmers.co.kr/learn/courses/30/lessons/12912
# 두 정수 사이의 합

def solution(a, b):
    answer = 0

    if a > b: a, b = b, a

    for i in range(a, b+1):
        answer += i

    return answer