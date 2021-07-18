class MapSum:
    """
    https://leetcode.com/problems/map-sum-pairs/
    
    java solution:
    https://leetcode.com/problems/map-sum-pairs/discuss/107513/Java-solution-Trie
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=self.TrieNode()
        

    def insert(self, key: str, val: int) -> None:
        cur=self.root
        for c in key:
            next=None
            if c not in cur.children:
                next=self.TrieNode()
                cur.children[c]=next
            else:
                next=cur.children[c]
            cur=next
        cur.is_Word=True
        cur.value=val


        

    def sum(self, prefix: str) -> int:
        cur=self.root
        for c in prefix:
            next=None
            if c not in cur.children:
                return 0
            else:
                next=cur.children[c]
            cur=next
        return self.dfs(cur)

    def dfs(self, node):
        _sum=0
        for k,v in node.children.items():
            _sum+=self.dfs(node.children[k])
        return _sum+node.value
        
    
    class TrieNode:
        def __init__(self):
            self.children={}
            self.is_Word=False
            self.value=0
if __name__ == "__main__":
    c=MapSum()
    c.insert('apple',3)
    print(c.sum('ap'))#3
    c.insert('app',2)
    print(c.sum("ap"))#5


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)