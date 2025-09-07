class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        if not self.queue:
            self.queue.append(x)
        else:
            self.queue.append(x)
            for _ in range(len(self.queue) - 1):
                t = self.queue.pop(0)
                self.queue.append(t)

    def pop(self) -> int:
        return self.queue.pop(0)

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
