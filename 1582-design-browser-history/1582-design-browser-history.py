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
        steps = min(steps, len(self.back_history))
        for _ in range(steps):
            self.front_history.append(self.current)
            self.current = self.back_history.pop()
        return self.current

    def forward(self, steps: int) -> str:
        steps = min(steps, len(self.front_history))
        for _ in range(steps):
            self.back_history.append(self.current)
            self.current = self.front_history.pop()
        return self.current
