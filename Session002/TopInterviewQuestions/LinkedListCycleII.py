# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    https://leetcode.com/problems/linked-list-cycle-ii/description/
    """
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        slow=head
        fast=head
        while True:
            slow=slow.next
            if slow is None:
                return None
            fast=fast.next
            if fast is None:
                return None
            fast=fast.next
            if fast is None:
                return None

            if fast==slow:
                slow2=head
                while slow!=slow2:
                    slow=slow.next
                    slow2=slow2.next
                return slow

        