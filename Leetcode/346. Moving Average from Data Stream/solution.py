class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        # Have a counter that represent the total sum
        self.counter = 0
        # Have a list with all the numbers and a pointer
        self.array = []
        # The pointer will represent the begining of the window
        self.window_star = 0
        

    def next(self, val: int) -> float:
        self.array.append(val)
        # the slower pointer is moved when the difference with the last index is bigger than the window
        if len(self.array) - self.window_star > self.size:
            # and the counter is decreased when this move happens by the number in the first pointer
            self.counter -= self.array[self.window_star]
            self.window_star += 1
        
        self.counter += val
        return self.counter / (self.size if len(self.array) >= self.size else len(self.array))
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)