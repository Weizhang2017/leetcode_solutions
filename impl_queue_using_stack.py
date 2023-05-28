class MyQueue:

    def __init__(self):
        self.l1 = []
        

    def push(self, x: int) -> None:
        self.l1.append(x)

    def pop(self) -> int:
        l2 = []
        while self.l1:
            l2.append(self.l1.pop())

        a = l2.pop()
        while l2:
            self.l1.append(l2.pop())
        return a

    def peek(self) -> int:
        return self.l1[0]

    def empty(self) -> bool:
        return self.l1 == []
