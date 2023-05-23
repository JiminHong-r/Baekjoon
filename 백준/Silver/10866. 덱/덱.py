import sys

class Deque:
    def __init__(self):
        self.dq = []

    def push_front(self, x):
        self.dq.insert(0, x)

    def push_back(self, x):
        self.dq.append(x)

    def pop_front(self):
        if (self.empty()):
            return (-1)
        else:
            return (self.dq.pop(0))

    def pop_back(self):
        if (self.empty()):
            return (-1)
        else:
            return (self.dq.pop())

    def size(self):
        return (len(self.dq))
    
    def empty(self):
        if (len(self.dq) == 0):
            return (1)
        else:
            return (0)
    
    def front(self):
        if (self.empty()):
            return (-1)
        else:
            return (self.dq[0])

    def back(self):
        if (self.empty()):
            return (-1)
        else:
            return (self.dq[len(self.dq) - 1])

d = Deque()
t = int(sys.stdin.readline())
for i in range(t):
    cmd = sys.stdin.readline().split()
    if (cmd[0] == "push_front"):
        d.push_front(int(cmd[1]))
    elif (cmd[0] == "push_back"):
        d.push_back(int(cmd[1]))
    elif (cmd[0] == "pop_front"):
        print(d.pop_front())
    elif (cmd[0] == "pop_back"):
        print(d.pop_back())
    elif (cmd[0] == "size"):
        print(d.size())
    elif (cmd[0] == "empty"):
        print(d.empty())
    elif (cmd[0] == "front"):
        print(d.front())
    elif (cmd[0] == "back"):
        print(d.back())