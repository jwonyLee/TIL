// https://www.acmicpc.net/problem/2460
// 지능형 기차 2
import Foundation

var arr = [[Int]]()
for _ in 0..<10 {
    arr.append(readLine()!.components(separatedBy: " ").map { Int($0)! })
}
var max = arr.removeFirst()[1]
var now = max

for station in arr {
    now = now - station[0] + station[1]
    if now > max {
        max = now
    }
}

print(max)
