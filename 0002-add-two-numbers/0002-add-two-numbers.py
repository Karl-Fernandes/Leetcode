# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        pointer = dummy
        carry = 0

        while l1 and l2:
            total = l1.val + l2.val + carry
            pointer.next = ListNode(total % 10)
            carry = total // 10
            l1, l2 = l1.next, l2.next
            pointer = pointer.next

        while l1:
            total = l1.val + carry
            pointer.next = ListNode(total % 10)
            carry = total // 10
            l1, pointer = l1.next, pointer.next

        while l2:
            total = l2.val + carry
            pointer.next = ListNode(total % 10)
            carry = total // 10
            l2, pointer = l2.next, pointer.next    

        if carry:
            pointer.next = ListNode(carry)

        return dummy.next


