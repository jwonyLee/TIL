// https://www.acmicpc.net/problem/10807
// 개수 세기

let n = Int(readLine()!)
var arr = readLine()!.split(separator: " ").map{ Int(String($0))! }
var cnt = Array(repeating: 0, count: 201)
let v = Int(readLine()!)!

for a in arr {
    cnt[100+a] += 1
}

print(cnt[100+v])