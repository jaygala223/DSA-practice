# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast = slow =ListNode(-1)
        fast.next = slow.next = head
        
        for i in range(1, n+1):
            fast = fast.next
            
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        if slow.next == head: return head.next
        
        slow.next = slow.next.next
        
        return head