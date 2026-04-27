import sys
input = sys.stdin.readline

class node:
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None
        self.parent = None

class tree:
    def __init__(self):
        self.root = None
        
    # 부모를 찾아 자식을 달아줌
    def insert(self, parent_key, left_key, right_key):
        # 트리가 비어있다면 루트 노드 생성
        if self.root is None:
            self.root = node(parent_key)
        
        # 부모 노드를 탐색
        parent_node = self.search_node(self.root, parent_key)
        
        # 부모 노드를 찾았다면 자식들을 추가
        if parent_node is not None:
            if left_key != '.':
                parent_node.left = node(left_key)
                parent_node.left.parent = parent_node
            if right_key != '.':
                parent_node.right = node(right_key)
                parent_node.right.parent = parent_node


    def search_node(self, current, x):
        if current is None:
            return None
        
        if current.key == x:
            return current
        
        # 크기 비교가 아닌 왼쪽을 먼저 끝까지 찾음
        left_result = self.search_node(current.left, x)
        if left_result is not None:
            return left_result
            
        # 왼쪽 서브트리에 없다면 오른쪽 서브트리를 찾음
        return self.search_node(current.right, x)

    # 순회 로직
    def preorder(self, current):
        if current is not None:
            print(current.key, end='')
            self.preorder(current.left)
            self.preorder(current.right)

    def inorder(self, current):
        if current is not None:
            self.inorder(current.left)
            print(current.key, end='')
            self.inorder(current.right)

    def postorder(self, current):
        if current is not None:
            self.postorder(current.left)
            self.postorder(current.right)
            print(current.key, end='')


N = int(input().strip())

my_tree = tree()

for i in range(N):
    p, l, r = input().split()
    my_tree.insert(p, l, r)

my_tree.preorder(my_tree.root)
print()
my_tree.inorder(my_tree.root)
print()
my_tree.postorder(my_tree.root)