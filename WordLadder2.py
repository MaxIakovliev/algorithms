

import string

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        dictr=set(wordList)
        res=list()
        nodeNeibors={}
        distance={}
        solution=list()
        dictr.add(beginWord)
        self.bfs(beginWord, endWord, dictr,nodeNeibors,distance)
        self.dfs(beginWord, endWord, nodeNeibors, distance, solution, res)
        return res

    def bfs(self, start, end,dictr,nodeNeibors, distince):
        for s in dictr:
            nodeNeibors[s]=list()
        
        queue=list()
        queue.append(start)
        distince[start]=0

        while len(queue)!=0:
            count= len(queue)
            found=False
            for i in range(count):
                cur=queue.pop(0)
                curDistance=distince[cur]
                neighbors=self.getNeighbors(cur, dictr)
                for neighbor  in neighbors:
                     
                    nodeNeibors[cur].append(neighbor)
                    if neighbor not in distince:
                        distince[neighbor]=curDistance+1
                        if end==neighbor:
                            found=True
                        else:
                            queue.append(neighbor)

                if found:
                    break
    def getNeighbors(self, node, dictr):
        res=list()
        chs=[c for c in node]
        for ch in string.ascii_lowercase:
            for i  in range(len(chs)):
                if chs[i]==ch:
                    continue
                old_ch=chs[i]
                chs[i]=ch
                if ''.join(chs) in dictr:
                    res.append(''.join(chs))
                chs[i]=old_ch
        return res

    
    def dfs(self, cur:str, end:str,  nodeNeighors:set, distance:set, solution:list, res:list):
        solution.append(cur)
        if end==cur:
            res.append([c for c in solution])
        else:
            for next in nodeNeighors[cur]:
                if distance[next]==distance[cur]+1:
                    self.dfs(next, end, nodeNeighors,distance, solution, res)
        del solution[len(solution)-1]


               
      
if __name__ =="__main__":
    c=Solution()
    print(c.findLadders("hit","cog", ["hot","dot","dog","lot","log","cog"]))
