# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s=head
        f=head
        while(f.next and f.next.next):
            f=f.next.next
            s=s.next
        prevleft=None
        ss=s.next
        curr=ss
        s.next=None
        while(curr):
            temp=curr.next
            curr.next=prevleft
            prevleft=curr
            curr=temp
        l1=head
        while(prevleft):
            temp1=l1.next
            temp2=prevleft.next
            l1.next=prevleft
            prevleft.next=temp1
            l1=temp1
            prevleft=temp2