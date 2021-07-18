class Solution(object):
    """
    https://leetcode.com/problems/redundant-connection-ii/
    solutions:
    https://leetcode.com/problems/redundant-connection-ii/discuss/155920/Python-both-DFS-and-Union-Find-solution
    """
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        candidate=[]
        self.parent=[0]*(len(edges)+1)
        for u,v in edges:
            if self.parent[v]!=0:
                candidate.append([self.parent[v],v])
                candidate.append([u,v])
            else:
                self.parent[v]=u
        if candidate!=[]:
            b1=self.findCycle(candidate[0][1])
            return candidate[0] if b1 else candidate[1]
        else:
            cycles=self.dfs(edges[0][0])
            for i in reversed(range(len(edges))):
                if tuple(edges[i]) in cycles:
                    return edges[i]

    def findCycle(self, node):
        seen={}
        while node!=0:
            if node in seen:
                return True
            seen[node]=1
            node=self.parent[node]
        return False
    
    def dfs(self, v):
        seen={}
        while v not in seen:
            seen[v]=1
            v=self.parent[v]
        edges={}
        u1,v1=self.parent[v],v
        while (u1,v1) not in edges:
            edges[(u1,v1)]=1
            u1,v1=self.parent[u1],u1
        return edges


        