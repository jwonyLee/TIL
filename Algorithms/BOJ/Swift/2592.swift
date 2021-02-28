// https://www.acmicpc.net/problem/2592
// 대표값
import Foundation

var dict: [Int: Int] = [:]
var sum = 0
for _ in 0..<10 {
    let n = Int(readLine()!)!
    sum += n
    dict[n, default: 0] += 1
}
let max = dict.max { a, b in a.value < b.value }!.key
print(sum/10)
print(max)