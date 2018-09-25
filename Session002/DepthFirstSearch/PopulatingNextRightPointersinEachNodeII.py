# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        def dfs(node,level):
            if node is None:
                return
            dfs(node.left, level+1)
            dfs(node.right,level+1)
            if level not in self.data:
                self.data[level]=[]
            self.data[level].append(node)
        
        def link():
            for k,v in self.data.items():
                for i in range(0,len(v)):
                    if i+1>=len(v):
                        v[i].next=None
                    else:
                        v[i].next=v[i+1]
        
        self.data={}
        dfs(root,0)
        link()
