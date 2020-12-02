// https://www.acmicpc.net/problem/10799
// 쇠막대기
let str = Array(readLine()!)
var s: [String] = []
var cnt = 0
for (i, c) in str.enumerated() {
    if c == "(" {
        s.append(String(c))
    } else {
        s.removeLast()
        if str[i-1] == "(" {
            cnt += s.count
        } else {
            cnt += 1
        }
    }
}
print(cnt)