# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        data=[]
        cur=head
        while cur is not None:
            data.append(cur)
            cur=cur.next
        if len(data)==0:
            return None
        if len(data)==1:
            return data[0]
            
        if len(data) %2==0:
            return data[len(data//2)]
        else:
            return data[len(data//2)+1]

