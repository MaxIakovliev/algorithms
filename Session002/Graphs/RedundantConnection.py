class Solution:
    """
    https://leetcode.com/problems/redundant-connection/
    """
    #correct solutions
    def findRedundantConnection2(self, edges: 'List[List[int]]') -> 'List[int]':
        visited=set()
        visited.add(edges[0][0])
        visited.add(edges[0][1])
        edges.pop(0)
        dup=list()
        i=0
        while i<len(edges):
            if edges[i][0] in visited or edges[i][1] in visited:
                if edges[i][0] in visited and edges[i][1] in visited:
                    dup.append(edges[i])
                    edges.pop(i)
                else:
                    visited.add(edges[i][0])
                    visited.add(edges[i][1])
                    edges.pop(i)
                i=0
            else:
                i+=1
        return dup[-1]



if __name__ == "__main__":
    c=Solution()
    print(c.findRedundantConnection2([[1,2], [1,3], [2,3]]))#[2,3]
    print(c.findRedundantConnection2([[1,2], [2,3], [3,4], [1,4], [1,5]]))#[1,4]
    print(c.findRedundantConnection2([[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]]))#[4,10]
    print(c.findRedundantConnection2([[1,5],[3,4],[3,5],[4,5],[2,4]]))#[4,5]

        