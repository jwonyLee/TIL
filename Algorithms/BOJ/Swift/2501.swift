// https://www.acmicpc.net/problem/2501
// 약수 구하기
import Foundation

var nums = readLine()!.components(separatedBy: " ").map { Int($0)! }
var stack = [Int]()
for i in 1...nums[0] {
    if nums[0] % i == 0 {
        stack.append(i)
    }
    if stack.count == nums[1] {
        break
    }
}

if stack.count < nums[1] {
    print(0)
} else {
    print(stack[nums[1]-1])
}

