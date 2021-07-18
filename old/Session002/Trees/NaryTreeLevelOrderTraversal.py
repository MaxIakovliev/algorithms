class Solution:
    """
    https://leetcode.com/problems/n-ary-tree-level-order-traversal/
   
    bfs solution:
    https://leetcode.com/problems/n-ary-tree-level-order-traversal/discuss/256358/python-BFS-96-ms
    dfs solution:
    https://leetcode.com/problems/n-ary-tree-level-order-traversal/discuss/155927/Beat-100-of-Java-DFS-(recursive)
    """
    def levelOrder(self, root: 'Node'):
        def dfs_solution(node, level):
            if node is None:
                return 
            tmp=[]
            if len(self.res)>level:
                self.res[level].append(node.val)
                
            else:
                tmp.append(node.val)
                self.res.append(tmp)
            for i in range(len(node.children)):
                dfs_solution(node.children[i], level+1)
            return

        def bfs_solution(node):
            if node is None:
                return []
            q=[]
            q.append(node)
            while len(q)>0:
                tmp=[]
                for i in range(len(q)):
                    node=q.pop(0)
                    tmp.append(node.val)
                    q.extend(node.children)
                
                self.res.append(tmp)
            return            
        
        self.res=[]
        bfs_solution(root)
        # dfs_solution(root, 0)
        return self.res
        

      