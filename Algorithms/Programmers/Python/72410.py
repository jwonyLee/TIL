# https://programmers.co.kr/learn/courses/30/lessons/72410?language=swift
# 신규 아이디 추천
def removeSpecialCharacters(string):
    special = "qwertyuioplkjhgfdsazxcvbnm1234567890-_."
    filter = ""
    for char in string:
        if char in special:
            filter += char
    return filter

def removeDot(string):
    filter = ""
    for char in string:
        if filter and filter[-1] == "." and char == ".":
            continue
        filter += char
        
    return filter

def removeFirstLastDot(string):
    filter = list(string)
    if filter and filter[0] == ".":
        filter.pop(0)
    if filter and filter[-1] == ".":
        filter.pop()
    return ''.join(filter)

def solution(new_id):
    answer = new_id
    # 모든 대문자를 소문자로
    answer = answer.lower()
    # '!', '@', '#', '*' 제거
    answer = removeSpecialCharacters(answer)
    # '...', '..'을 '.'으로 치환
    answer = removeDot(answer)
    # 아이디의 처음이나 끝에 위치한 '.' 제거
    answer = removeFirstLastDot(answer)
    # 아이디가 빈 문자열이라면 "a" 대입
    if len(answer) < 1:
        answer = "a"
    # 길이가 16자 이상이면,
    if len(answer) >= 15:
        answer = answer[:15]
    answer = removeFirstLastDot(answer)
    # 2
    if len(answer) < 3:
        while len(answer) != 3:
            answer += answer[-1]
    return answer