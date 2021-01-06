# https://programmers.co.kr/learn/courses/30/lessons/12930
# 이상한 문자 만들기
def solution(s):
    answer = ''
    words = s.split(" ")
    for word in words:
        for w in range(len(word)):
            if w == 0 or w % 2 == 0:
                answer += word[w].upper()
            else:
                answer += word[w].lower()
        answer += " "
    return answer[:len(answer)-1]