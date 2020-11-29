// https://www.acmicpc.net/problem/10808
// 알파뱃 개수

let word = readLine()!.lowercased()
var count = Array(repeating: 0, count: 26)

for char in word.utf16 {
    count[Int(char) - 97] += 1
}

print(count.map { String($0) }.joined(separator: " "))
