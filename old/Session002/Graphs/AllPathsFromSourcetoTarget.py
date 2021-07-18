class Solution:
    """
    https://leetcode.com/problems/all-paths-from-source-to-target/
    solution:
    https://leetcode.com/problems/all-paths-from-source-to-target/discuss/118713/Java-DFS-Solution
    """
    def allPathsSourceTarget(self, graph: 'List[List[int]]') -> 'List[List[int]]':
        def dfs(graph, node:int, result:list, path:list):
            if node==len(graph)-1:
                tmp=path[:]
                result.append(tmp)
                return
            for next_node in graph[node]:
                path.append(next_node)
                dfs(graph,next_node,result,path)
                path.pop()
            return
        res=[]
        path=[0]
        dfs(graph,0,res,path)
        return res

        