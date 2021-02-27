# https://programmers.co.kr/learn/courses/30/lessons/42576
# 완주하지 못한 선수

def solution(participant, completion):
    answer = ''
    dict = {}

    for p in participant:
        dict[p] = dict.get(p, 0) + 1

    for c in completion:
        if c in dict:
            dict[c] -= 1

    for key, value in dict.items():
        if value > 0:
            answer += key
    return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
