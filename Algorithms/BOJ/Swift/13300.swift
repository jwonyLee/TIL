// https://www.acmicpc.net/problem/13300
// 방 배정

import Foundation

let n = readLine()!.split(separator: " ").map { Int(String($0))! }
var girls = Array(repeating: 0, count: 7)
var boys = Array(repeating: 0, count: 7)

for _ in 0..<n[0] {
    let s = readLine()!.split(separator: " ").map { Int(String($0))! }
    if s[0] == 1 {
        boys[s[1]] += 1
    } else {
        girls[s[1]] += 1
    }
}

var gcnt = 0
var bcnt = 0

girls.forEach {
    gcnt += Int(ceil(Double($0) / Double(n[1])))
}

boys.forEach {
    bcnt += Int(ceil(Double($0) / Double(n[1])))
}

print(gcnt + bcnt)
