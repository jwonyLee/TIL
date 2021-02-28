// https://programmers.co.kr/learn/courses/30/lessons/70128
// 내적
import Foundation

func solution(_ a:[Int], _ b:[Int]) -> Int {
    var answer = 0
    for (x, y) in zip(a, b) {
        answer += x * y
    }
    return answer
}