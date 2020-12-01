// https://www.acmicpc.net/problem/4949
// 균형잡힌 세상
var word = readLine()!
while !word.isEmpty {
    var flag = true
    var s: [String] = []
    for c in word {
        if c == "(" || c == "[" {
            s.append(String(c))
        } else if c == ")" {
            if !s.isEmpty {
                if s.removeLast() != "(" {
                    flag = false
                }
            } else {
                flag = false
            }
        } else if c == "]" {
            if !s.isEmpty {
                if s.removeLast() != "[" {
                    flag = false
                }
            } else {
                flag = false
            }
        }
    }
    
    if !s.isEmpty {
        print("no")
    } else if flag == true {
        print("yes")
    } else if flag == false {
        print("no")
    }
    
    word = readLine()!
    word.removeLast()
}