class BrowserHistory:

    def __init__(self, homepage: str):
        self.current_page = 0
        self.pages = [homepage] 

    def visit(self, url: str) -> None:
        if self.current_page != len(self.pages) - 1:
            del self.pages[self.current_page + 1:]
        
        self.pages.append(url)
        self.current_page += 1

    def back(self, steps: int) -> str:
        self.current_page = 0 if steps > self.current_page else self.current_page - steps
        return self.pages[self.current_page]

    def forward(self, steps: int) -> str:
        self.current_page = len(self.pages) - 1 if steps > (len(self.pages) - self.current_page - 1) else self.current_page + steps
        return self.pages[self.current_page]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)