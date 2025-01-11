from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        
        # Initialize the queue with the root
        queue = deque([root])
        
        while queue:
            size = len(queue)  
            
            for i in range(size):
                node = queue.popleft()
                
              
                if i < size - 1:
                    node.next = queue[0]
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root
