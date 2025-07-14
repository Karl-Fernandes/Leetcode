# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        if not lists:
            return None
        
        for i in range(1, len(lists)):
            lists[i] = self.mergeTwoLists(lists[i], lists[i-1])
        
        return lists[-1]



    def mergeTwoLists(self, list1, list2):
        if not list1 and not list2:
            return None
        
        if not list2:
            return list1
        
        if not list1:
            return list2

        dummy = ListNode()
        pointer = dummy

        while list1 and list2:
            if list1.val >= list2.val:
                pointer.next = list2
                list2 = list2.next
            else:
                pointer.next = list1
                list1 = list1.next
            pointer = pointer.next
        
        if list1:
            pointer.next = list1
        
        if list2:
            pointer.next = list2
        
        return dummy.next

        