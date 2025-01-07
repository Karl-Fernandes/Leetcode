# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        binary = ""
        decimal = 0
        while head:
            binary += str(head.val)
            head = head.next
        
        for bit in binary:
            decimal = (decimal << 1)
            decimal |= int(bit)
        
        return decimal

        
        


        
        