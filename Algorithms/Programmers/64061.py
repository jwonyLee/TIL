# https://programmers.co.kr/learn/courses/30/lessons/64061
# 크레인 인형뽑기 게임
def solution(board, moves):
    answer = 0
    max_depth = len(board) - 1
    basket = []

    for move in moves:
        cur = move - 1
        depth = 0

        # 인형이 있을 때까지 & 바닥에 닿을 때 까지 크레인 내리기
        while depth < max_depth and board[depth][cur] == 0:
            depth += 1
            
        if board[depth][cur] != 0: # 인형이 있음
            basket.append(board[depth][cur])
            board[depth][cur] = 0

        # 바스켓 확인하기
        if len(basket) > 1 and basket[-1] == basket[-2]:
            basket.pop()
            basket.pop()
            answer += 2
            
    return answer