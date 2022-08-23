# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # method 2
        
        if head is None:
            return None
        
        odd,even=head,head.next
        temp=even
        
        while even!=None and even.next!=None:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
            
        odd.next=temp
        
        return head
        
        
        
        
        
        
        
        
        # method 1
        
        temp=head
        arr=[]
        dummy=ListNode(-1)
        while temp:
            arr.append(temp.val)
            temp=temp.next
        print(arr)
        
        l=None
        
        
        arr.reverse()
        if len(arr)%2!=0:
            for i in range(len(arr)):
                if i%2!=0:
                    l=ListNode(arr[i],l)
            for i in range(len(arr)):
                if i%2==0:
                    l=ListNode(arr[i],l)
        else:
            
            for i in range(len(arr)):
                if i%2==0:
                    l=ListNode(arr[i],l)
            for i in range(len(arr)):
                if i%2!=0:
                    l=ListNode(arr[i],l)
        return l
            
