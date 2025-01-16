class Logger:

    def __init__(self):
        self._mem = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self._mem:
            self._mem[message] = timestamp
            return True
        elif self._mem[message] + 10 > timestamp:
            return False
        else:
            self._mem[message] = timestamp
            return True

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)