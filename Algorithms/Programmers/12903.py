# https://programmers.co.kr/learn/courses/30/lessons/12903
# 가운데 글자 가져오기

def solution(s):
    answer = ''
    mid = int(len(s) / 2)

    if len(s)% 2 == 0: # 단어의 길이가 짝수 일 경우
        answer = s[mid-1] + s[mid]
    else:
        answer = s[mid]

    return answer

print(solution('abcde'))
print(solution('qwer'))