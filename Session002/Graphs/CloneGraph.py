
"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
class Solution:
    """
    https://leetcode.com/problems/clone-graph/
    """
    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.bfs(node)
        

    def bfs(self,node):
        queue=[]
        queue.append(node)
        copy=Node(node.val,[])
        visited={node:copy}
        while len(queue)>0:
            cur=queue.pop(0)
            for nb in cur.neighbors:
                if nb not in visited:
                    queue.append(nb)
                    nb_copy=Node(nb.val,[])
                    visited[nb]=nb_copy
                visited[cur].neighbors.add(visited[nb])
        return visited[node]

                