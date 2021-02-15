// https://www.acmicpc.net/problem/1357
// 뒤집힌 덧셈
import Foundation

func rev(_ str: String) -> Int {
    Int(String(str.reversed()))!
}

let nums = readLine()!.components(separatedBy: " ")
print(rev(String(rev(nums[0]) + rev(nums[1]))))