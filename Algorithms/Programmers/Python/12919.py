# https://programmers.co.kr/learn/courses/30/lessons/12919
# 서울에서 김서방 찾기

def solution(seoul):
    answer = "김서방은 %d에 있다" % seoul.index("Kim")
    return answer

print(solution(["Jane", "Kim"]))
