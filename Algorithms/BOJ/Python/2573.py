# https://www.acmicpc.net/problem/2573
# 빙산(미해결)
import sys
n, m = map(int, sys.stdin.readline().strip().split(" ")) # 빙산의 크기
board = [] # 빙산
year = 0 # 시간
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

def countIce():
    arr = [[False for _ in range(m)] for _ in range(n)]
    cnt = 0

    def dfs(i, j):
        discovered = []
        stack = [[i, j]]
        while stack:
            x, y = stack.pop()
            nx = x - 1
            ny = y
            
            if nx >= 0 and nx < n and ny >= 0 and ny < m and board[nx][ny] != 0 and arr[nx][ny] == False:
                if [nx, ny] not in discovered:
                    discovered.append([nx, ny])
                    stack.append([nx, ny])
                    arr[nx][ny] = True

            nx = x
            ny = y + 1
            if nx >= 0 and nx < n and ny >= 0 and ny < m and board[nx][ny] != 0 and arr[nx][ny] == False:
                if [nx, ny] not in discovered:
                    discovered.append([nx, ny])
                    stack.append([nx, ny])
                    arr[nx][ny] = True

            nx = x + 1
            ny = y
            if nx >= 0 and nx < n and ny >= 0 and ny < m and board[nx][ny] != 0 and arr[nx][ny] == False:
                if [nx, ny] not in discovered:
                    discovered.append([nx, ny])
                    stack.append([nx, ny])
                    arr[nx][ny] = True

            nx = x
            ny = y - 1
            if nx >= 0 and nx < n and ny >= 0 and ny < m and board[nx][ny] != 0 and arr[nx][ny] == False:
                if [nx, ny] not in discovered:
                    discovered.append([nx, ny])
                    stack.append([nx, ny])
                    arr[nx][ny] = True

    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and arr[i][j] == False:
                cnt += 1
                if cnt >= 2: return cnt
                dfs(i, j)

    return cnt


if countIce() >= 2:
    print(0)
else:
    while True:
        # 각 칸의 녹아야하는 수 구하기
        melt = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if board[i][j] != 0:
                    if i - 1 >= 0 and i - 1 < n and j >= 0 and j < m: 
                        if board[i-1][j] == 0 and board[i][j] > 0:
                            melt[i][j] += 1
                    if i >= 0 and i < n and j + 1 >= 0 and j + 1 < m: 
                        if board[i][j+1] == 0 and board[i][j] > 0:
                            melt[i][j] += 1
                    if i + 1 >= 0 and i + 1 < n and j >= 0 and j < m: 
                        if board[i+1][j] == 0 and board[i][j] > 0:
                            melt[i][j] += 1
                    if i >= 0 and i < n and j - 1 >= 0 and j - 1 < m: 
                        if board[i][j-1] == 0 and board[i][j] > 0:
                            melt[i][j] += 1

        # 1년 지나기(위에서 구한 수 빙산에 빼주기)
        for i in range(n):
            for j in range(m):
                if board[i][j] >= melt[i][j]:
                    board[i][j] -= melt[i][j]
                else:
                    board[i][j] = 0

        # 빙산이 두 덩어리로 나뉘었는지 확인하기
        year += 1
        if countIce() >= 2: # 빙산의 개수가 2 이상인 경우 시간 출력 후 탈출
            print(year)
            break
        elif sum(sum(board,[])) == 0: # 빙산의 합이 0인 경우 탈출
            print(0)
            break