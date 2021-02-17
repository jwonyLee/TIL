// https://www.acmicpc.net/problem/3460
// 이진수
import Foundation

let t = Int(readLine()!)!
for _ in 0..<t {
    var n = Array(String(Int(readLine()!)!, radix: 2))
    var idx = 0

    while !n.isEmpty {
        let item = n.removeLast()
        if item == "1" {
            print(idx, terminator:" ")
        }
        idx += 1
    }
}