# 너비 우선 탐색 (Breadth-First Search)
class Node:
    
    def __init__(self):
        self.marked = False
        self.adjacent = []

def search(root):
    queue = []
    root.marked = True
    queue.append(root)

    while queue:
        r = Node(queue.pop(0))
        visit(r)
        for n in r.adjacent:
            if not n.marked:
                n.marked = True
                queue.append(n)