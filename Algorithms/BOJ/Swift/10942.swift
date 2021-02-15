// https://www.acmicpc.net/problem/10942
// 팰린드롬?
// 스위프트는 시간보정이 되어있지 않아서 풀 수 없음
import Foundation

let n = Int(readLine()!)
let nums = readLine()!.replacingOccurrences(of: " ", with: "")
let m = Int(readLine()!)!

for _ in 0..<m {
    let index = readLine()!.components(separatedBy: " ").map { Int($0)! - 1 }
    let split = nums[index[0]...index[1]]
    if split == String(split.reversed()) {
        print(1)
    } else {
        print(0)
    }
}

extension String {
    subscript(r: Range<Int>) -> String {
        get {
            let startIndex = self.index(self.startIndex, offsetBy: r.lowerBound)
            let endIndex = self.index(self.startIndex, offsetBy: r.upperBound)

            return String(self[startIndex..<endIndex])
        }
    }

    subscript(r: ClosedRange<Int>) -> String {
        get {
            let startIndex = self.index(self.startIndex, offsetBy: r.lowerBound)
            let endIndex = self.index(self.startIndex, offsetBy: r.upperBound)

            return String(self[startIndex...endIndex])
        }
    }
}