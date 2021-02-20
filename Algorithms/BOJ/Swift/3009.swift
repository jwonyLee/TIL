// https://www.acmicpc.net/problem/3009
// 네 번째 점
import Foundation
var x = Dictionary<Int, Int>()
var y = Dictionary<Int, Int>()
for _ in 0..<3 {
    let num = readLine()!.split(separator: " ").map { Int($0)! }
    x[num[0], default: 0] += 1
    y[num[1], default: 0] += 1
}
for (a, b) in zip(x.filter { $0.value == 1 }, y.filter { $0.value == 1}) {
    print("\(a.key) \(b.key)")
}