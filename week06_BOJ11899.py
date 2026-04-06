import sys
input = sys.stdin.readline

st = input().rstrip()

stack = []

for i in st:
    if i == ")":
        if len(stack) > 0 and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(i)
    elif i == "(":
        stack.append(i)

print(len(stack))