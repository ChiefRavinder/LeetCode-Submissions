# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        slow=head
        fast=head
        prevslow=None
        while fast and fast.next:
            prevslow=slow
            slow=slow.next
            fast=fast.next.next
        prevslow.next=prevslow.next.next
        return head
        
        