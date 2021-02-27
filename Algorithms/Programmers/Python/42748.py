# https://programmers.co.kr/learn/courses/30/lessons/42748
# K번째 수

def solution(array, commands):
    answer = []
    for c in commands:
        answer.append(sorted(array[c[0] -1 : c[1]])[c[2]-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))