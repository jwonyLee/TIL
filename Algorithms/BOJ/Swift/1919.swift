// https://www.acmicpc.net/problem/1919
// 애너그램 만들기
var word1 = readLine()!
var word2 = readLine()!
var cnt1 = Array(repeating: 0, count: 26)
var cnt2 = Array(repeating: 0, count: 26)

word1.utf16.forEach { cnt1[Int($0) - 97] += 1}
word2.utf16.forEach { cnt2[Int($0) - 97] += 1}

var cnt = 0

for (c1, c2) in zip(cnt1, cnt2) {
    cnt += abs(c1-c2)
}

print(cnt)