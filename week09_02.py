import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)

class node:
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None
        self.parent = None
        
class tree:
    def __init__(self):
        self.root = None
        
    def insert(self, x):
        if (self.root is None):
            self.root = node(x)
        else:
            self.insert_node(self.root, x)
            
    # insert_node 구현
    def insert_node(self, current, x):
        # 현재 노드의 키값보다 작으면 왼쪽으로
        if current.key > x:
            if current.left is None:
                current.left = node(x)
                current.left.parent = current
            else:
                self.insert_node(current.left, x)
        # 현재 노드의 키값보다 크면 오른쪽으로
        else:
            if current.right is None:
                current.right = node(x)
                current.right.parent = current
            else:
                self.insert_node(current.right, x)

    # 후위 순회 (왼쪽 -> 오른쪽 -> 루트)
    def postorder(self, current):
        if current is not None:
            self.postorder(current.left)
            self.postorder(current.right)
            print(current.key)


my_tree = tree()

while True:
    try:
        val = int(input().strip())
        my_tree.insert(val)
    except:
        break

# 루트부터 후위 순회 시작
my_tree.postorder(my_tree.root)