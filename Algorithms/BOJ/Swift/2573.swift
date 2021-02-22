// https://www.acmicpc.net/problem/2573
// 빙산
// 현재는 시간초과로 풀리지 않았음 -> 틀린 코드..
import Foundation

let size = readLine()!.split(separator: " ").map { Int($0)! } // 빙산의 크기
var board = [[Int]]() // 빙산
var year = 0 // 시간
for _ in 0..<size[0] {
    board.append(readLine()!.split(separator: " ").map { Int($0)! })
}

func dfs(_ i: Int, _ j: Int, _ arr:inout [[Bool]]) {
    var discovered = Set<Array<Int>>()
    var stack = [[i, j]]
    while !stack.isEmpty {
        let v = stack.removeLast()
        var nx = v[0] - 1
        var ny = v[1]
        if nx >= 0 && nx < size[0] && ny >= 0 && ny < size[1] && board[nx][ny] != 0 && arr[nx][ny] == false {
            if !discovered.contains([nx, ny]) {
                discovered.insert([nx, ny])
                stack.append([nx, ny])
                arr[nx][ny] = true
            }
        }

        nx = v[0]
        ny = v[1] + 1
        if nx >= 0 && nx < size[0] && ny >= 0 && ny < size[1] && board[nx][ny] != 0 && arr[nx][ny] == false {
            if !discovered.contains([nx, ny]) {
                discovered.insert([nx, ny])
                stack.append([nx, ny])
                arr[nx][ny] = true
            }
        }

        nx = v[0] + 1
        ny = v[1]
        if nx >= 0 && nx < size[0] && ny >= 0 && ny < size[1] && board[nx][ny] != 0 && arr[nx][ny] == false {
            if !discovered.contains([nx, ny]) {
                discovered.insert([nx, ny])
                stack.append([nx, ny])
                arr[nx][ny] = true
            }
        }

        nx = v[0]
        ny = v[1] - 1
        if nx >= 0 && nx < size[0] && ny >= 0 && ny < size[1] && board[nx][ny] != 0 && arr[nx][ny] == false {
            if !discovered.contains([nx, ny]) {
                discovered.insert([nx, ny])
                stack.append([nx, ny])
                arr[nx][ny] = true
            }
        }
    }
}

func countIce() -> Int {
    var arr = Array(repeating: Array(repeating: false, count: size[1]), count: size[0])
    var cnt = 0
    for i in 0..<size[0] {
        for j in 0..<size[1] {
            if board[i][j] != 0 && arr[i][j] == false {
                cnt += 1
                if cnt >= 2 { return cnt }
                dfs(i, j, &arr)
            }

        }
    }
    return cnt
}

if countIce() >= 2 {
    print(0)
} else {
    while true {
        // 각 칸의 녹아야하는 수 구하기
        var melt = Array(repeating: Array(repeating: 0, count: size[1]), count: size[0]) // 매년 녹는 수를 저장 -> 따로 저장하는 이유는 모든 칸이 한꺼번에 녹기 때문에
        for i in 0..<size[0] {
            for j in 0..<size[1] {
                if board[i][j] != 0 {
                    if i - 1 >= 0 && i - 1 < size[0] && j >= 0 && j < size[1] { if board[i-1][j] == 0 && board[i][j] > 0 { melt[i][j] += 1 } }
                    if i >= 0 && i < size[0] && j + 1 >= 0 && j + 1 < size[1] { if board[i][j+1] == 0 && board[i][j] > 0 { melt[i][j] += 1 } }
                    if i + 1 >= 0 && i + 1 < size[0] && j >= 0 && j < size[1] { if board[i+1][j] == 0 && board[i][j] > 0 { melt[i][j] += 1 } }
                    if i >= 0 && i < size[0] && j - 1 >= 0 && j - 1 < size[1] { if board[i][j-1] == 0 && board[i][j] > 0 { melt[i][j] += 1 } }
                }
            }
        }

        // 1년 지나기(위에서 구한 수 빙산에 빼주기)
        for i in 0..<size[0] {
            for j in 0..<size[1] {
                if board[i][j] >= melt[i][j] {
                    board[i][j] -= melt[i][j]
                } else {
                    board[i][j] = 0
                }
            }
        }

        // 빙산이 두 덩어리로 나뉘었는지 확인하기
        year += 1
        if countIce() >= 2 { // 빙산의 개수가 2 이상인 경우 시간 출력 후 탈출
            print(year)
            break
        } else if board.joined().reduce(0, +) == 0 { // 빙산의 합이 0인 경우 탈출
            print(0)
            break
        }
    }
}
