# https://programmers.co.kr/learn/courses/30/lessons/12981
# 영어 끝말잇기
from collections import defaultdict
def solution(n, words):
    answer = []
    person = defaultdict(int)
    overlap = set()
    # 첫번째 사람만 따로 처리
    overlap.add(words[0])
    person[0] += 1
    for i in range(1, len(words)):
        if not words[i] in overlap and words[i-1][-1] == words[i][0]: # 중복이 아닌 경우
            overlap.add(words[i])
            person[i%n] += 1
        else:
            person[i%n] += 1
            return [i%n + 1, person[i%n]]
            
    return [0, 0]