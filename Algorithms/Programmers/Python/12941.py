# https://programmers.co.kr/learn/courses/30/lessons/12941
# 최솟값 만들기
def solution(A,B):
    answer = 0

    for a, b in zip(sorted(A), sorted(B, reverse=True)):
        answer += a*b

    return answer