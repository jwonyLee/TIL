// https://www.acmicpc.net/problem/1159
// 농구 경기
import Foundation

let n = Int(readLine()!)!
var dict = Dictionary<Character, Int>()

for _ in 0..<n {
    let name = readLine()!
    dict[name.first!] = dict[name.first!, default: 0] + 1
}

if dict.filter({ $0.value >= 5 }).count > 0 {
    print(dict.filter { $0.value >= 5 }.map { String($0.key) }.sorted().joined())
} else {
    print("PREDAJA")
}