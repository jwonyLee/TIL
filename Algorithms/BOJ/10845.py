# https://www.acmicpc.net/problem/10845
# 큐
import sys

class Queue:
    def __init__(self):
        self.list = []

    # 정수 X를 큐에 넣는 연산이다.
    def push(self, x):
        self.list.append(x)
    
    # 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    def pop(self):
        if not self.list:
            print(-1)
        else:
            print(self.list.pop(0))
    
    # 큐에 들어있는 정수의 개수를 출력한다.
    def size(self):
        print(len(self.list))

    # 큐가 비어있으면 1, 아니면 0을 출력한다.
    def empty(self):
        if not self.list:
            print(1)
        else:
            print(0)
    
    # 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    def front(self):
        if not self.list:
            print(-1)
        else:
            print(self.list[0])

    # 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    def back(self):
        if not self.list:
            print(-1)
        else:
            print(self.list[len(self.list) - 1])

queue = Queue()

n = int(sys.stdin.readline().strip())

for _ in range(0, n):
    command = sys.stdin.readline().strip().split(" ")

    if command[0] == "push":
        queue.push(command[1])
    elif command[0] == "pop":
        queue.pop()
    elif command[0] == "size":
        queue.size()
    elif command[0] == "empty":
        queue.empty()
    elif command[0] == "front":
        queue.front()
    else: # back
        queue.back()
