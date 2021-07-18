# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=None
        cur=None

        while l1 is not None or l2 is not None:
            if l1 is not None and l2 is not None:
                if l1.val<l2.val:
                    if head is None:
                        cur=l1
                    else:
                        cur.next=l1
                        cur=cur.next
                    l1=l1.next
                else:
                    if head is None:
                        cur=l2
                    else:
                        cur.next=l2
                        cur=cur.next
                    l2=l2.next
            elif l1 is not None and l2 is None:
                if head is None:
                    cur=l1
                else:
                    cur.next=l1
                    cur=cur.next
                l1=l1.next
            else :
                if head is None:
                    cur=l2
                else:
                    cur.next=l2
                    cur=cur.next
                l2=l2.next

            if head is None:
                head=cur
        if cur is not None:
            cur.next=None
        return head
            