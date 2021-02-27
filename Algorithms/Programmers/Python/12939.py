# https://programmers.co.kr/learn/courses/30/lessons/12939
# 최댓값과 최솟값
def solution(s):
    numbers = list(map(int, s.split(" ")))
    return "{} {}".format(min(numbers), max(numbers))