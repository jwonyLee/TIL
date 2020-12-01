// https://www.acmicpc.net/problem/10828
// 스택
var stack = Array(repeating: 0, count:  10000)
var pos = 0

func push(_ x: Int) {
    stack[pos] = x
    pos += 1
}

func pop() -> Int {
    if pos < 1 { // 스택이 비어있으면
        return -1
    }
    pos -= 1
    return stack[pos]
}

func size() -> Int {
    return pos
}

func top() -> Int {
    if pos < 1 {
        return -1
    }
    
    return stack[pos-1]
}

func empty() -> Int {
    return pos < 0 ? 1 : 0
}

for _ in 0..<Int(readLine()!)! {
    let op = readLine()!.split(separator: " ")
    switch op[0] {
    case "push":
        push(Int(op[1])!)
    case "pop":
        print(pop())
    case "size":
        print(size())
    case "empty":
        print(empty())
    case "top":
        print(top())
    default: break
    }
}