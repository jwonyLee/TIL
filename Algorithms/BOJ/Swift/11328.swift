// https://www.acmicpc.net/problem/11328
// Strfry

let n = Int(readLine()!)!

for _ in 0..<n {
    let word = readLine()!.split(separator: " ").map { String($0) }
    if word[0].sorted() == word[1].sorted() {
        print("Possible")
    } else {
        print("Impossible")
    }
}
