# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        while head is not None and head.val==val:
            head=head.next
        cur=head
        prev=cur
        while cur is not None:
            if cur.val==val:
                prev.next=cur.next
            else:
                prev=cur
            cur=cur.next
        return head

if __name__ =="__main__":
    c=Solution()
    data=[1,2,6,3,4,5,6]
    head=ListNode(data[0])
    cur=head
    for n in range(1, len(data)):
        node=ListNode(data[n])
        cur.next=node
        cur=cur.next
    res= c.removeElements(head,6)
    data=[]
    while res is not None:
        data.append(res.val)
        res=res.next
    print(data)

    data=[1,2,2,1]
    head=ListNode(data[0])
    cur=head
    for n in range(1, len(data)):
        node=ListNode(data[n])
        cur.next=node
        cur=cur.next
    res= c.removeElements(head,1)
    data=[]
    while res is not None:
        data.append(res.val)
        res=res.next
    print(data)
    
    data=[1,1]
    head=ListNode(data[0])
    cur=head
    for n in range(1, len(data)):
        node=ListNode(data[n])
        cur.next=node
        cur=cur.next
    res= c.removeElements(head,1)
    data=[]
    while res is not None:
        data.append(res.val)
        res=res.next
    print(data)



       
            
        
        