# https://programmers.co.kr/learn/courses/30/lessons/42862
# 체육복

def solution(n, lost, reserve):
    answer = 0

    for l in lost:
        prev = l - 1
        next = l + 1
        if l in reserve:
            lost.remove(l)
            reserve.remove(l)
        elif prev in reserve:
            lost.remove(l)
            reserve.remove(prev)
        elif next in reserve:
            lost.remove(l)
            reserve.remove(next)
    answer = n - len(lost)
    return answer

