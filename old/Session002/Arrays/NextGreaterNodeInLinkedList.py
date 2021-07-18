# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    """
    https://leetcode.com/problems/next-greater-node-in-linked-list/
    """
    def nextLargerNodes(self, head: 'ListNode') -> 'List[int]':
        res=[]
        st=[]
        cur=head
        i=0
        while cur:
            item={'val':cur.val, 'idx':i}
            if len(st)==0:
                st.append(item)
                cur=cur.next
                continue
            res.append(0)
            while len(st)>0 and cur.val>st[-1]['val']:
                res[st[-1]['idx']]=cur.val
                st.pop()

            i+=1
            item={'val':cur.val, 'idx':i}
            st.append(item)
            cur=cur.next
        res.append(0)
        return res
if __name__ == "__main__":

    dat=[2,1,5]
    head=ListNode(dat[0])
    cur=head
    for i in range(1,len(dat)):
        cur.next=ListNode(dat[i])
        cur=cur.next
    c=Solution1()
    print(c.nextLargerNodes(head))#[5,5,0]


    dat=[2,7,4,3,5]
    head=ListNode(dat[0])
    cur=head
    for i in range(1,len(dat)):
        cur.next=ListNode(dat[i])
        cur=cur.next
    c=Solution1()
    print(c.nextLargerNodes(head))#[7,0,5,5,0]

