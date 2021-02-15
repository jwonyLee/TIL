// https://www.acmicpc.net/problem/10987
// 모음의 개수
import Foundation
let word = readLine()!
print(word.filter { ["a","i","o","u","e"].contains($0) }.count)