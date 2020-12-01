// https://www.acmicpc.net/problem/5430
// AC
// 참고: https://www.acmicpc.net/board/view/25456
for _ in 0..<Int(readLine()!)! {
    let p = readLine()!
    let n = Int(readLine()!)!
    var x = readLine()!
    var range = x.index(after: x.startIndex)..<x.index(before: x.endIndex)
    var arr = x[range].split(separator: ",").map { String($0) }
    var flag = false
    var error = false
    var h = 0
    var e = n
    for s in p {
        if s == "R" {
            flag = !flag
        } else if s == "D" {
            if h != e {
                if flag { e -= 1}
                else { h += 1}
            } else {
                error = true
            }
        }
    }
    if !error {
        if flag {
            arr[h..<e].reverse()
            print("[\(arr[h..<e].joined(separator: ","))]")
        } else {
            print("[\(arr[h..<e].joined(separator: ","))]")
        }
    } else {
        print("error")
    }
}