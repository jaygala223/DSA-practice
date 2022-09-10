# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy, cnt = head, 0
        while dummy:
            dummy = dummy.next
            cnt += 1
        
        front_n = cnt - n + 1
        cnt = 1
        
        if front_n == 1: return head.next
        
        dum1 = ListNode(-1)
        dum1.next = head
        dum2 = head
        while dum2:
            if cnt == front_n:
                dum1.next = dum2.next
                break
            
            dum2 = dum2.next
            dum1 = dum1.next
            cnt += 1
        return head