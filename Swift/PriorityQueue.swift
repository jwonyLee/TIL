// https://swexpertacademy.com/main/code/referenceCode/referenceCodeDetail.do?referenceId=test02&category=DataStructure
import Foundation

struct PriorityQueue {

    var maxSize = 100

    lazy var heap = Array(repeating: 0, count: maxSize)
    var heapSize = 0

    init() {
        heapSize = 0
    }

    init(_ max: Int) {
        self.maxSize = max
        self.heapSize = 0
        heap = Array(repeating: 0, count: maxSize)
    }

    mutating func heapPush(_ value: Int) -> Int {
        if heapSize + 1 > maxSize {
            print("queue is full")
            return 0
        }

        heap[heapSize] = value

        var current = heapSize
        while current > 0 && heap[current] < heap[(current - 1) / 2] {
            let temp = heap[(current - 1) / 2]
            heap[(current - 1) / 2] = heap[current]
            heap[current] = temp
            current = (current - 1) / 2
        }

        heapSize = heapSize + 1

        return 1
    }

    mutating func heapPop(_ value:inout Int) -> Int {
        if heapSize <= 0 {
            return -1
        }

        value = heap[0]
        heapSize = heapSize - 1

        heap[0] = heap[heapSize]

        var current = 0
        while current * 2 + 1 < heapSize {
            var child = 0
            if current * 2 + 2 == heapSize {
                child = current * 2 + 1
            } else {
                child = heap[current * 2 + 1] < heap[current * 2 + 2] ? current * 2 + 1 : current * 2 + 2
            }

            if heap[current] < heap[child] {
                break
            }

            let temp = heap[current]
            heap[current] = heap[child]
            heap[child] = temp

            current = child
        }

        return 1
    }

}

let t = Int(readLine()!)!
for _ in 0..<t {
    let n = Int(readLine()!)!

    var pQueue = PriorityQueue()

    let values = readLine()!.split(separator: " ").map { Int(String($0))! }
    for v in values {
        pQueue.heapPush(v)
    }

    for _ in 0..<n {
        var value = 0
        pQueue.heapPop(&value)
        print(value, terminator: " ")
    }
    print()
}