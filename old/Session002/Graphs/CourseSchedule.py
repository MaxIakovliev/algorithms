from collections import defaultdict
class Solution:
    # class Graph():
    #     def __init__(self, V):
    #         self.V=V
    #         self.adj=defaultdict(list)
        
    #     def addAdj(self, a,b):
    #         self.adj[a].append(b)
    #         self.adj[b].append(a)

    #     def isCycle(self):
    #         visited=[False]*self.V
    #         recStack=[False]*self.V
    #         for node in range(self.V):
    #             if not visited[node]:
    #                 if self.isCyclic(node, visited,recStack):
    #                     return True
    #             return False
    #     def isCyclic(self, node, visited, recStack):
    #         visited[node]=True
    #         recStack[node]=True
    #         for neigbour in self.adj[node]:
    #             if visited[neigbour]==False:
    #                 if self.isCyclic(neigbour,visited,recStack):
    #                     return True
    #             elif recStack[neigbour]==True:
    #                 return True
    #         recStack[node]=False
    #         return False

    class Graph(): 
        """
        https://leetcode.com/problems/course-schedule/
        """
        def __init__(self,vertices): 
            self.graph = defaultdict(list) 
            self.V = vertices 
    
        def addEdge(self,u,v): 
            self.graph[u].append(v) 
    
        def isCyclicUtil(self, v, visited, recStack): 
    
            # Mark current node as visited and  
            # adds to recursion stack 
            visited[v] = True
            recStack[v] = True
    
            # Recur for all neighbours 
            # if any neighbour is visited and in  
            # recStack then graph is cyclic 
            for neighbour in self.graph[v]: 
                if visited[neighbour] == False: 
                    if self.isCyclicUtil(neighbour, visited, recStack) == True: 
                        return True
                elif recStack[neighbour] == True: 
                    return True
    
            # The node needs to be poped from  
            # recursion stack before function ends 
            recStack[v] = False
            return False
    
        # Returns true if graph is cyclic else false 
        def isCyclic(self): 
            visited = [False] * self.V 
            recStack = [False] * self.V 
            for node in range(self.V): 
                if visited[node] == False: 
                    if self.isCyclicUtil(node,visited,recStack) == True: 
                        return True
            return False

    def canFinish(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'bool':
        g=self.Graph(numCourses)
        for item in prerequisites:
            g.addEdge(item[0],item[1])
        
        return not g.isCyclic()
if __name__ =="__main__":
    c=Solution()
    print(c.canFinish(2,[[1,0]]))
    print(c.canFinish(2,[[1,0],[0,1]]))

        