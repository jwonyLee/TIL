// https://www.acmicpc.net/problem/2573
// 빙산
// 현재는 시간초과로 풀리지 않았음 -> 틀린 코드..
import Foundation

let size = readLine()!.split(separator: " ").map { Int($0)! } // 빙산의 크기
let x = [-1, 0, 1, 0]
let y = [0, 1, 0, -1]
var board = [[Int]]() // 빙산
var year = 0 // 시간
for _ in 0..<size[0] {
    board.append(readLine()!.split(separator: " ").map { Int($0)! })
}

func bfs(_ i: Int, _ j: Int, _ arr:inout [[Bool]]) {
    var discovered = [[i, j]]
    var queue = [[i, j]]
    while !queue.isEmpty {
        let v = queue.removeFirst()
        for (dx, dy) in zip(x, y) {
            let nx = v[0] + dx
            let ny = v[1] + dy
            if nx < 0 || nx >= size[0] || ny < 0 || ny >= size[1] || board[nx][ny] == 0 { continue }
            if arr[nx][ny] == true { continue }
            if !discovered.contains([nx, ny]) {
                discovered.append([nx, ny])
                queue.append([nx, ny])
                arr[nx][ny] = true
            }
        }
    }
}

// 처음 입력받았을 때 검사하기
func countIce() -> Int {
    var arr = Array(repeating: Array(repeating: false, count: size[1]), count: size[0])
    var cnt = 0
    cntBfs: for i in 0..<size[0] {
        for j in 0..<size[1] {
            if board[i][j] != 0 && arr[i][j] == false {
                if cnt >= 2 {
                    break cntBfs
                }
                bfs(i, j, &arr)
                cnt += 1
            }

        }
    }
    return cnt
}

if countIce() >= 2 {
    print(0)
} else {
    while true {
        // 각 칸의 녹는 수 구하기
        var melt = Array(repeating: Array(repeating: 0, count: size[1]), count: size[0]) // 매년 녹는 수를 저장 -> 따로 저장하는 이유는 모든 칸이 한꺼번에 녹기 때문에
        for i in 0..<size[0] {
            for j in 0..<size[1] {
                if board[i][j] != 0 {
                    for (dx, dy) in zip(x, y) {
                        let nx = i + dx
                        let ny = j + dy
                        if nx < 0 || nx >= size[0] || ny < 0 || ny >= size[1] { continue }
                        if board[i+dx][j+dy] == 0 && board[i][j] > 0 {
                            melt[i][j] += 1
                        }
                    }
                }
            }
        }

        // 위에서 구한 수를 빼주기
        for i in 0..<size[0] {
            for j in 0..<size[1] {
                if board[i][j] >= melt[i][j] {
                    board[i][j] -= melt[i][j]
                } else {
                    board[i][j] = 0
                }
            }
        }

        // 빙산 개수 구하기
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