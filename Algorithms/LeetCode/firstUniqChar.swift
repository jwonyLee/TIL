class Solution {
    func firstUniqChar(_ s: String) -> Int {
        var dict = [Character: Int]()
        for char in s {
            dict[char, default: 0] += 1
        }

        for (i, v) in s.enumerated() {
            if dict[v] == 1 {
                return i
            }
        }
        return -1
    }
}