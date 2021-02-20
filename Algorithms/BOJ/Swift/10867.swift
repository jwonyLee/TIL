// https://www.acmicpc.net/problem/10867
// 중복 빼고 정렬하기
import Foundation
_ = readLine()!
var nums = readLine()!.split(separator: " ").map { Int($0)! }
for chr in Array(Set(nums)).sorted() {
    print(chr, terminator: " ")
}