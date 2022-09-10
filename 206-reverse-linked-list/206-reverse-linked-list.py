# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None
        p1 = head
        p2 = head
        
        while p2:
            p1 = p2
            p2 = p2.next
            p1.next = dummy
            dummy = p1
            
        return p1
        