# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(head):    
            prev = None
            while head:
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
            return prev
        
        temp = prev = reverse(head)
        
        maxi = temp.val
        while temp.next:
            if temp.next.val < maxi:
                temp.next = temp.next.next
            else:
                temp = temp.next
                maxi = temp.val
        return reverse(prev)