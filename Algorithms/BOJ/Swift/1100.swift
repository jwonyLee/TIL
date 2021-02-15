// https://www.acmicpc.net/problem/1100
// 하얀 칸
import Foundation

var board: Array<Array<Character>> = Array()
var count: Int = 0

for _ in 0..<8 {
    let str = readLine()!
    board.append(Array(str))
}

for i in 0..<8 {
    for j in 0..<8 {
        if (i + j) % 2 == 0 && board[i][j] == "F" {
            count += 1
        }
    }
}

print(count)
