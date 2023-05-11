import sys

n = int(input())

class Queue:
    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if (self.empty() == 1):
            return (-1)
        else:
            return (self.queue.pop(0))

    def size(self):
        return len(self.queue)

    def empty(self):
        if (self.size() < 1):
            return (1)
        else:
            return (0)

    def front(self):
        if (self.size() < 1):
            return (-1)
        else:
            return (self.queue[0])
    
    def back(self):
        if (self.size() < 1):
            return (-1)
        else:
            return (self.queue[self.size() - 1])

queue = Queue()

for i in range(n):
    str = sys.stdin.readline().split()
    cmd = str[0]
    if (cmd == "push"):
        queue.push(str[1])
    elif (cmd == "pop"):
        print(queue.pop())
    elif (cmd == "size"):
        print(queue.size())
    elif (cmd == "empty"):
        print(queue.empty())
    elif (cmd == "front"):
        print(queue.front())
    elif (cmd == "back"):
        print(queue.back())