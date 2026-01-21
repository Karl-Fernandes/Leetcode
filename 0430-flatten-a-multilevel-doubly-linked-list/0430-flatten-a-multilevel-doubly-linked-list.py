class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        self.dfs(head)
        return head

    def dfs(self, node):
        curr = node
        last = node 
        
        while curr:
            next_node = curr.next

            if curr.child:
                child_tail = self.dfs(curr.child)

                curr.next = curr.child
                curr.child.prev = curr
                
                if next_node:
                    child_tail.next = next_node
                    next_node.prev = child_tail
                    
                curr.child = None
                last = child_tail
                
            else:
                last = curr
            
            curr = curr.next
            
        return last