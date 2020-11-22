# https://www.acmicpc.net/problem/10866
# 덱
import sys

class Deque:
    def __init__(self):
        self.list = []
    
    # 정수 X를 덱의 앞에 넣는다.
    def push_front(self, x):
        self.list.insert(0, x)

    # 정수 X를 덱의 뒤에 넣는다.
    def push_back(self, x): 
        self.list.append(x)

    # 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    def pop_front(self):
        if not self.list:
            print(-1)
        else:
            print(self.list.pop(0))

    # 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    def pop_back(self):
        if not self.list:
            print(-1)
        else:
            print(self.list.pop())

    # 덱에 들어있는 정수의 개수를 출력한다.
    def size(self): 
        print(len(self.list))

    # 덱이 비어있으면 1을, 아니면 0을 출력한다.
    def empty(self): 
        if not self.list:
            print(1)
        else:
            print(0)

    # 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    def front(self): 
        if not self.list:
            print(-1)
        else:
            print(self.list[0])

    # 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    def back(self): 
        if not self.list:
            print(-1)
        else:
            print(self.list[len(self.list) - 1])


deque = Deque()

n = int(sys.stdin.readline())

for _ in range(0, n):
    command = sys.stdin.readline().strip().split()

    if command[0] == "push_front":
        deque.push_front(command[1])
    elif command[0] == "push_back":
        deque.push_back(command[1])
    elif command[0] == "pop_front":
        deque.pop_front()
    elif command[0] == "pop_back":
        deque.pop_back()
    elif command[0] == "size":
        deque.size()
    elif command[0] == "empty":
        deque.empty()
    elif command[0] == "front":
        deque.front()
    elif command[0] == "back":
        deque.back()