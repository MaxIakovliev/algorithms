class Node:
    def __init__(self, k, v):
        self.key=k
        self.val=v
        self.next=None
        self.prev=None

class LRUCache:
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.dict=dict()
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
      
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            node=self.dict[key]
            self._remove(node)
            self._add(node)
            return node.val    
        return -1    

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict:
            self._remove(self.dict[key])
        
        n=Node(key,value)
        self._add(n)
        self.dict[key]=n
        if len(self.dict)>self.capacity:
            n=self.head.next
            self._remove(n)
            del self.dict[n.key]
    
    def _add(self,node):
        p=self.tail.prev
        p.next=node
        self.tail.prev=node
        node.prev=p
        node.next=self.tail
    
    def _remove(self, node):
        p=node.prev
        n=node.next
        p.next=n
        n.prev=p
        
            

    
    def check(self):
        pass
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ =="__main__":
    cache=LRUCache(2)
    # cache.put(1, 1)
    # cache.put(2, 2)
    # print(cache.get(1)==1)  #       // returns 1
    # cache.put(3, 3)          #    // evicts key 2
    # print(cache.get(2)==-1) #       // returns -1 (not found)
    # cache.put(4, 4)          #    // evicts key 1
    # print(cache.get(1)==-1) #       // returns -1 (not found)
    # print(cache.get(3)==3)  #       // returns 3
    # print(cache.get(4)==4)  #      // returns 4
names=["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
inputs=[[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
exp=[None,None,None,None,None,None,-1,None,19,17,None,-1,None,None,None,-1,None,-1,5,-1,12,None,None,3,5,5,None,None,1,None,-1,None,30,5,30,None,None,None,-1,None,-1,24,None,None,18,None,None,None,None,-1,None,None,18,None,None,-1,None,None,None,None,None,18,None,None,-1,None,4,29,30,None,12,-1,None,None,None,None,29,None,None,None,None,17,22,18,None,None,None,-1,None,None,None,20,None,None,None,-1,18,18,None,None,None,None,20,None,None,None,None,None,None,None]
c=None
for i in range(len(names)):
    if names[i]=="LRUCache":
        c=LRUCache(inputs[i][0])
    elif names[i]=="put":
        c.put(inputs[i][0],inputs[i][1])
    elif names[i]=="get":
        res=c.get(inputs[i][0])
        
        print("{0}- exp={1}; actual={2}; {3}".format(str(i),str(exp[i]),str(res),res==exp[i]))
        
    
