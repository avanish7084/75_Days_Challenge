
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=0
        temp=head
        while temp!=None:
            c+=1
            temp=temp.next
            
        prev=None
        curr=head
        print(c)
        if c-n-1<0:
            return curr.next
        for i in range(c-n):
            prev=curr
            curr=curr.next
        prev.next=curr.next
        return head
