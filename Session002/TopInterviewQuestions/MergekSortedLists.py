# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from queue import PriorityQueue
class Solution:
    """
    https://leetcode.com/problems/merge-k-sorted-lists/description/
    """

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pq=PriorityQueue()
        dummy=ListNode(None)
        tail=dummy

        for item in lists:
            while item is not None:
                pq.put(item.val)
                item=item.next
        while not pq.empty():
            tail.next=ListNode(pq.get())
            tail=tail.next
        return dummy.next

    def mergeKLists2(self, lists):
        data=[]
        for item in lists:
            while item is not None:
                data.append(item.val)
                item=item.next
        data.sort()
        dummy=ListNode(None)
        tail=dummy
        for item in data:
            tail.next=ListNode(item)
            tail=tail.next
        return dummy.next
