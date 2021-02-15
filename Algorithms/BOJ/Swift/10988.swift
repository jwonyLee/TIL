// https://www.acmicpc.net/problem/10988
// 팰린드롬인지 확인하기
import Foundation

let words = readLine()!
print("\(words == String(words.reversed()) ? 1 : 0)")