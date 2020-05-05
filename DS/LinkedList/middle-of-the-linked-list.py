   def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return
        fast=slow=head
        
        while fast and fast.next:
            fast,slow=fast.next.next,slow.next
        return slow
            
