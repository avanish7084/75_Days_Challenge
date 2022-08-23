
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # Method 2
        
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            
        # reverse  second half node    
        prev=nextp=None
        while slow:
            nextp=slow.next
            slow.next=prev
            prev=slow
            slow=nextp
        new_second_half_reverse_node=prev
        
        while new_second_half_reverse_node:
            if new_second_half_reverse_node.val!=head.val:
                return False
            new_second_half_reverse_node=new_second_half_reverse_node.next
            head=head.next
        return True
        
        # Method 1
        
        
        curr=head
        res=head
        prev=nextp=None
        arr=[]
        while res:
            arr.append(res.val)
            res=res.next
        while curr:
            nextp=curr.next
            curr.next=prev
            prev=curr
            curr=nextp
        
        i=0
        while prev: 
            if arr[i]!=prev.val:
                return False
            i+=1
            prev=prev.next
        return True
        
