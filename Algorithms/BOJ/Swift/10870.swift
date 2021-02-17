// https://www.acmicpc.net/problem/10870
// 피보나치 수 5
import Foundation

var f = Array(repeating: 0, count: 21)
f[1] = 1
f[2] = 1

for i in 3..<21 {
    f[i] = f[i-1] + f[i-2]
}

let n = Int(readLine()!)!
print(f[n])
