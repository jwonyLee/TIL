// https://www.acmicpc.net/problem/1926
// 그림
let size = readLine()!.split(separator: " ").map {Int( String($0))! }
var grid: [[String]] = []
for _ in 0..<size[0] {
    grid.append(contentsOf: Array(arrayLiteral: readLine()!.split(separator: " ").map({ String($0) })))
}

func bfs(_ i: Int, _ j: Int) {
    if i < 0 || i >= size[0] || j < 0 || j >= size[1] || grid[i][j] != "1" {
        return
    }
    grid[i][j] = "0"
    max += 1
    
    bfs(i+1, j)
    bfs(i-1, j)
    bfs(i, j+1)
    bfs(i, j-1)
}

var cnt = 0
var max = 0
var total = 0
if grid[0].count > 0 {
    for i in 0..<size[0] {
        for j in 0..<size[1] {
            if grid[i][j] == "1" {
                max = 0
                bfs(i, j)
                cnt += 1
                if total < max {
                    total = max
                }
            }
        }
    }
}
print(cnt)
print(total)
