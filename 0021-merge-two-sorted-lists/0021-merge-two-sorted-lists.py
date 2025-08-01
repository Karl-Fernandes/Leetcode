# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2:
            return None
        
        if not list2:
            return list1
        
        if not list1:
            return list2

        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val >= list2.val:
                curr.next = ListNode(list2.val)
                list2 = list2.next
            else:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            curr = curr.next
      
        
        while list1:
            curr.next = ListNode(list1.val)
            curr = curr.next
            list1 = list1.next
        
        while list2:
            curr.next = ListNode(list2.val)
            curr = curr.next
            list2 = list2.next
        

        return dummy.next



        