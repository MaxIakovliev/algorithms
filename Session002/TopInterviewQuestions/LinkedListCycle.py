# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        slow=head
        fast=head
        
        while True:
            slow=slow.next
            if slow is None:
                return False
            fast=fast.next
            if fast is None:
                return False
            fast=fast.next
            if fast is None:
                return False
            if fast==slow:
                return True
