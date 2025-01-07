class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = homepage
        self.back_history = []
        self.front_history = []

        
        

    def visit(self, url: str) -> None:
        self.back_history.append(self.current)
        self.front_history = []
        self.current = url

        

    def back(self, steps: int) -> str:
        if steps <= len(self.back_history):
            for step in range(steps):
                temp = self.current
                self.current = self.back_history.pop()
                self.front_history.append(temp)
        else:
            for step in range(len(self.back_history)):
                temp = self.current
                self.current = self.back_history.pop()
                self.front_history.append(temp)
        
        return self.current

    def forward(self, steps: int) -> str:
        if steps <= len(self.front_history):
            for step in range(steps):
                temp = self.current
                self.current = self.front_history.pop()
                self.back_history.append(temp)
        else:
            for step in range(len(self.front_history)):
                temp = self.current
                self.current = self.front_history.pop()
                self.back_history.append(temp)

        
        return self.current
 

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)