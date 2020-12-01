// https://www.acmicpc.net/problem/10828
// 스택
var stack: [Int] = []

for _ in 0..<Int(readLine()!)! {
    let op = readLine()!.split(separator: " ")
    switch op[0] {
    case "push":
        stack.append(Int(op[1])!)
    case "pop":
        print(stack.isEmpty ? -1 : stack.removeLast())
    case "size":
        print(stack.count)
    case "empty":
        print(stack.isEmpty ? 1 : 0)
    case "top":
        print(stack.isEmpty ? -1 : stack.last!)
    default: break
    }
}