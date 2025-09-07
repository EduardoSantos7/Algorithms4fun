class StringIterator:

    def __init__(self, compressedString: str):
        chars = [c for c in compressedString if c.isalpha()]
        numbers = "".join([n if n.isnumeric() else "#" for n in compressedString[1:]]).split("#")
        self.string = "".join([char*int(number) for char, number in zip(chars, numbers) if number])
        self.current = 0

    def next(self) -> str:
        _next = ' '
        if self.current < len(self.string):
            _next = self.string[self.current]
            self.current += 1
        
        return _next

    def hasNext(self) -> bool:
        return self.current < len(self.string)
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()