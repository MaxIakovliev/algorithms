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
            if head is None:
                if  l1 is not None and l2 is not None and l1.val<l2.val:
                    head=l1
                    l1=l1.next
                    cur=head
                elif l1 is not None and l2 is not None and l1.val>l2.val:
                    head=l2
                    l2=l2.next
                    cur=head
                elif l1 is None and l2 is not None:
                    head=l2
                    l2=l2.next
                    cur=head
                else:
                    head=l1
                    l1=l1.next
                    cur=head
            elif l1 is not None and l2 is not None and l1.val<l2.val:
                cur.next=l1
                l1=l1.next
                cur=cur.next
            elif  l1 is not None and l2 is not None and l1.val>l2.val:
                cur.next=l2
                l2=l2.next
                cur=cur.next
            elif  l1 is None and l2 is not None:
                cur.next=l2
                l2=l2.next
                cur=cur.next
            else:
                cur.next=l1
                l1=l1.next
                cur=cur.next
        return head

                
                
                