import sys

n = int(input())

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if (self.empty() == 1):
            return (-1)
        else:
            return (self.stack.pop())

    def size(self):
        return len(self.stack)

    def empty(self):
        if (self.size() < 1):
            return (1)
        else:
            return (0)

    def top(self):
        if (len(self.stack) < 1):
            return (-1)
        else:
            return (self.stack[-1])

stack = Stack()

for i in range(n):
    str = sys.stdin.readline().split()
    cmd = str[0]
    if (cmd == "push"):
        stack.push(str[1])
    elif (cmd == "pop"):
        print(stack.pop())
    elif (cmd == "size"):
        print(stack.size())
    elif (cmd == "empty"):
        print(stack.empty())
    elif (cmd == "top"):
        print(stack.top())