class Node:
    def __init__(self, val: int, _next: Node = None):
        self.val = val
        self.next = _next


class MRUQueue:

    def __init__(self, n: int):
        self.head = Node(1)
        temp = self.head
        for val in range(2, n + 1):
            node = Node(val)
            temp.next = node
            temp = node
        self.tail = temp

    def fetch(self, k: int) -> int:
        if k == 1:
            if self.head.next != None:
                temp = self.head
                self.head = temp.next
                temp.next = None
                self.tail.next = temp
                self.tail = temp
                return temp.val
            else:
                return self.tail.val

        prev = self.head
        current = self.head.next

        while (k - 2) > 0:
            prev = current
            current = current.next
            k -= 1

        if current == self.tail:
            return self.tail.val

        prev.next = current.next
        current.next = None
        self.tail.next = current
        self.tail = current

        return self.tail.val


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
