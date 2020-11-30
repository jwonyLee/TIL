// https://www.acmicpc.net/problem/5397
// 키로거
let n = Int(readLine()!)!
for _ in 0..<n {
    let str = readLine()!
    var left: [String] = []
    var right: [String] = []
    for s in str {
        if s == "-" {
            if !left.isEmpty {
                left.removeLast()
            }
        } else if s == "<" {
            if !left.isEmpty {
                right.append(left.removeLast())
            }
        } else if s == ">" {
            if !right.isEmpty {
                left.append(right.removeLast())
            }
        } else { // Character
            left.append(String(s))
        }
    }
    print(left.joined() + right.reversed().joined())
}