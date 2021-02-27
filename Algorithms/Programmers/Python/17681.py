# https://programmers.co.kr/learn/courses/30/lessons/17681
# [1차] 비밀지도
def binArr(n, arr):
    binArr = []
    for a in arr:
        cnt = n - len(str(bin(a))[2:])
        temp = []
        while cnt != 0:
            temp.append(0)
            cnt -= 1
        for b in str(bin(a))[2:]:
            temp.append(int(b))
        binArr.append(temp)
    return binArr

def solution(n, arr1, arr2):
    answer = []
    arr1_bin = binArr(n, arr1)
    arr2_bin = binArr(n, arr2)
    ans = []
    for a, b in zip(arr1_bin, arr2_bin):
        temp = []
        for x, y in zip(a, b):
            temp.append(x | y)
        answer.append(temp)
    for a in answer:
        temp = ""
        for b in a:
            if b == 1:
                temp += "#"
            else:
                temp += " "
        ans.append(temp)
    
    return ans