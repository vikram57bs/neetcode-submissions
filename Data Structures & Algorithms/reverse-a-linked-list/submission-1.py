# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevleft=None
        curr=head
        if(head is None):
            return prevleft
        while(curr.next):
            nextt=curr.next
            curr.next=prevleft
            prevleft=curr
            curr=nextt
        curr.next=prevleft
        return curr