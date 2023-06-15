class OrderedStream:

    def __init__(self, n: int):
        self.length = n + 1
        self.stream = [None] * (n+1)
        self.output_index = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value

        while self.output_index < self.length and self.stream[self.output_index]:
            self.output_index += 1

        return self.stream[idKey:self.output_index]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
