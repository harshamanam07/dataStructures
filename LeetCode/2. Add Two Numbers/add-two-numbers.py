# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1,cur2=l1,l2
        to_return=ListNode(0)
        to_return_head=to_return
        carry=0
        
        while cur1 is not None and cur2 is not None:
            cur_sum=cur1.val+cur2.val+carry
            if cur_sum>=10:
                carry=1
                cur_sum=cur_sum%10
                
            else:
                carry=0
                to_return.next=ListNode(cur_sum)
            to_return.next=ListNode(cur_sum%10)
            cur1,cur2,to_return=cur1.next,cur2.next,to_return.next
        
        while cur1 is not None:
            cur_sum=cur1.val+carry
            if cur_sum>=10:
                carry=1
                to_return.next=ListNode(cur_sum%10)
            else:
                carry=0
                to_return.next=ListNode(cur_sum)
                
            cur1,to_return=cur1.next,to_return.next
        
        while cur2 is not None:
            cur_sum=cur2.val+carry
            if cur_sum>=10:
                carry=cur_sum//10
                to_return.next=ListNode(cur_sum%10)
            else:
                carry=0
                to_return.next=ListNode(cur_sum)
                
            cur2,to_return=cur2.next,to_return.next
            
        if carry==1:
            to_return.next=ListNode(1)
        return to_return_head.next        
                
            
            
