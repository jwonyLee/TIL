class Solution {
    func moveZeroes(_ nums: inout [Int]) {
        var arr = [Int]()
        var count = 0
        for num in nums {
            if num == 0 {
                count += 1
            } else {
                arr.append(num)
            }
        }
        for _ in 0..<count {
            arr.append(0)
        }
        nums = arr
    }
}