def solution(text):
    answer = []

    for t in text:
        if t == ' ':
            answer.append("%20")
            continue
        answer.append(t)

    return ''.join(answer)

print(solution("Mr John Smith"))