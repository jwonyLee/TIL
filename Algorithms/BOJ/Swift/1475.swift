// https://www.acmicpc.net/problem/1475
// 방 번호
import Foundation

let n = readLine()!
var num = Array(repeating: 0, count: 9)


n.forEach {
    if Int(String($0)) == 9 {
        num[6] += 1
    } else {
        num[Int(String($0))!] += 1
    }
}

var m = 0
for i in 0..<num.count {
    if i == 6 && num[i] >= 2 {
        num[i] = Int(ceil(Double(num[i]) / 2.0))
    }
    if m < num[i] {
        m = num[i]
    }
}

print(m)