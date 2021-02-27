# https://programmers.co.kr/learn/courses/30/lessons/12906
# 같은 숫자는 싫어

def solution(arr):
    answer = []
    for a in arr:
        if a not in answer:
            answer.append(a)
        if a != answer[len(answer) - 1]:
            answer.append(a)
    return answer


print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))