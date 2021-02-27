# https://programmers.co.kr/learn/courses/30/lessons/12916
# 문자열 내 p와 y의 개수

def solution(s):
    countP = 0
    countY = 0

    for i in s.lower():
        if i == 'p': countP += 1
        if i == 'y': countY += 1

    if countP == countY:
        return True
    return False