# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count=0
        tmp=list()
        cur=head
        while cur is not None:
            # if count>n:
            #     break
            tmp.append(cur)
            cur=cur.next
            count+=1

        if count==1 and n==1:
            return None
        
        if n==1:
            tmp[len(tmp)-n-1].next=None
            return head
        
        if n==len(tmp):
            head=None
            head=tmp[1]
            return head
        
        if n>0:
            tmp[len(tmp)-n-1].next=tmp[len(tmp)-n+1]
            return head

    

if __name__ =='__main__':
    s=Solution()
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
            self.head=self
        
        def add_to_the_end(self, val):
            cur=self.head
            while cur.next is not None:
                cur=cur.next
            cur.next=ListNode(val)
           
            
            
        
        def printLinkedList(self):
            cur =self.head
            while cur is not None:
                print (cur.val)
                cur=cur.next 
            
    ln=ListNode(1)
    ln.add_to_the_end(2)
    ln.add_to_the_end(3)
    ln.add_to_the_end(4)
    ln.add_to_the_end(5)
    s.removeNthFromEnd(ln,5)
    ln.printLinkedList()

        