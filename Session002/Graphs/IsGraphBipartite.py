class Solution:
    """
    https://leetcode.com/problems/is-graph-bipartite/
    
    Explanation:
    https://www.geeksforgeeks.org/bipartite-graph/s

    Solution:
    https://leetcode.com/problems/is-graph-bipartite/discuss/229340/BFS-Python
    """
    def isBipartite(self, graph: "List[List[int]]") -> bool:
        n=len(graph)
        self.nodes=[-1]*n
        def bfs(s):
            self.nodes[s]=0
            queue=[]
            queue.append(s)
            while len(queue)>0:
                cur=queue.pop(0)
                for t in graph(cur):
                    if self.nodes[t]==-1:
                        self.nodes[t]=self.nodes[cur]+1
                        queue.append(t)
                    elif self.nodes[t]==self.nodes[cur]:
                        return False
            return True
        for v in range(n):
            if self.nodes[v]==-1:
                if not bfs(v):
                    return False
        return True
        