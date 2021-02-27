# https://programmers.co.kr/learn/courses/30/lessons/12918
# 문자열 다루기 기본

def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            return True
        else:
            return False

    return False