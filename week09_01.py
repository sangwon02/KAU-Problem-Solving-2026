import sys
input = sys.stdin.readline

# 트리를 구성하는 기본 단위인 '노드' 클래스입니다.
class node:
    def __init__(self, x):
        self.key = x        # 노드의 값 (예: 'A', 'B' 등)
        self.left = None    # 왼쪽 자식 노드를 가리키는 포인터
        self.right = None   # 오른쪽 자식 노드를 가리키는 포인터

# 전체 트리를 관리하는 '트리' 클래스입니다.
class tree:
    def __init__(self):
        # 트리에 존재하는 모든 노드를 딕셔너리로 관리합니다.
        # 키(key)는 노드의 이름('A'), 값(value)은 실제 node 객체입니다.
        # 이렇게 하면 특정 이름의 노드를 O(1)의 속도로 빠르게 찾을 수 있습니다.
        self.nodes = {}
        
    # 트리에 새로운 노드와 그 자식들을 연결하는 메서드입니다.
    def add_node(self, parent_key, left_key, right_key):
        # 1. 부모 노드가 아직 트리에 없다면 새로 생성해서 딕셔너리에 넣습니다.
        if parent_key not in self.nodes:
            self.nodes[parent_key] = node(parent_key)
        
        # 부모 노드 객체를 가져옵니다.
        parent_node = self.nodes[parent_key]
        
        # 2. 왼쪽 자식이 있다면 ('.'이 아니라면)
        if left_key != '.':
            # 왼쪽 자식 노드가 트리에 없다면 새로 생성합니다.
            if left_key not in self.nodes:
                self.nodes[left_key] = node(left_key)
            # 부모 노드의 왼쪽 자식으로 연결합니다.
            parent_node.left = self.nodes[left_key]
            
        # 3. 오른쪽 자식이 있다면 ('.'이 아니라면)
        if right_key != '.':
            # 오른쪽 자식 노드가 트리에 없다면 새로 생성합니다.
            if right_key not in self.nodes:
                self.nodes[right_key] = node(right_key)
            # 부모 노드의 오른쪽 자식으로 연결합니다.
            parent_node.right = self.nodes[right_key]

    # 전위 순회 (Root -> Left -> Right)
    def preorder(self, current):
        if current is not None:
            print(current.key, end='')  # 1. 자기 자신(루트) 출력
            self.preorder(current.left) # 2. 왼쪽 자식 탐색
            self.preorder(current.right)# 3. 오른쪽 자식 탐색

    # 중위 순회 (Left -> Root -> Right)
    def inorder(self, current):
        if current is not None:
            self.inorder(current.left)  # 1. 왼쪽 자식 탐색
            print(current.key, end='')  # 2. 자기 자신(루트) 출력
            self.inorder(current.right) # 3. 오른쪽 자식 탐색

    # 후위 순회 (Left -> Right -> Root)
    def postorder(self, current):
        if current is not None:
            self.postorder(current.left)  # 1. 왼쪽 자식 탐색
            self.postorder(current.right) # 2. 오른쪽 자식 탐색
            print(current.key, end='')    # 3. 자기 자신(루트) 출력

# ================= 메인 실행 부분 =================

# 노드의 개수 N을 입력받습니다.
N = int(input().strip())

# 빈 트리를 하나 생성합니다.
my_tree = tree()

# N번 반복하면서 트리에 노드를 추가합니다.
for _ in range(N):
    # p: 부모, l: 왼쪽 자식, r: 오른쪽 자식
    p, l, r = input().split()
    my_tree.add_node(p, l, r)

# 문제의 조건에 따라 항상 'A'가 최상위 루트 노드입니다.
root_node = my_tree.nodes['A']

# 전위 순회 결과 출력
my_tree.preorder(root_node)
print() # 줄바꿈

# 중위 순회 결과 출력
my_tree.inorder(root_node)
print() # 줄바꿈

# 후위 순회 결과 출력
my_tree.postorder(root_node)