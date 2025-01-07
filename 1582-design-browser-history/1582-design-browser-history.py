class BrowserHistory:
    class Node:
        def __init__(self, url):
            self.url = url
            self.prev = None
            self.next = None

    def __init__(self, homepage: str):
        self.head = self.Node(homepage)  
        self.current = self.head

    def visit(self, url: str) -> None:
        new_node  = self.Node(url)
        new_node.prev = self.current
        self.current.next = new_node
        self.current = new_node

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.url

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.url
