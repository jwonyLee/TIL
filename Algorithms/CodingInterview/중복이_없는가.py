import sys

def solution():
    text = sys.stdin.readline().strip() # 문자열 입력

    dict = {} # 중복 여부를 체크할 딕셔너리 변수

    for c in text:
        if not dict.get(c): # dict에 문자가 없다면(한번도 등장하지 않았더라면)
            dict[c] = dict.get(c, True)
        else: # dict에 문자가 있다면(한 번 이상 등장했다면)
            dict[c] = False
            
    for v in dict.values():
        if not v: # 중복
            return False

    return True