import string
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        def bfs(start, end,dictr,nodeNeigbors,distance):
            def getNeigbours(word, dctr):
                res=[]
                chrs=[c for c in word]
                for ch in string.ascii_lowercase:
                    for i in range(len(chrs)):
                        if chrs[i]==ch:
                            continue
                        oldChr=chrs[i]
                        chrs[i]=ch
                        if "".join(chrs) in dctr:
                            res.append("".join(chrs))
                        chrs[i]=oldChr
                return res
               

            for s in dictr:
                nodeNeigbors[s]=list()
            queue=list()
            queue.append(start)
            distance[start]=0
            while len(queue)!=0:
                count=len(queue)
                found=False
                for i in range(count):
                    cur=queue.pop(0)
                    curDistance=distance[cur]
                    neighbors=getNeigbours(cur,dictr)
                    for neighbor in neighbors:
                        nodeNeigbors[cur].append(neighbor)
                        if neighbor not in distance:
                            distance[neighbor]=curDistance+1
                            if neighbor==end:
                                found=True
                            else:
                                queue.append(neighbor)
                    if found:
                        break
        
        def dfs(cur:str,end:str,nodeNeigbors:set,distance:set, solution:list, res:list):
            solution.append(cur)
            if end==cur:
                res.append([item for item in solution])
            else:
                for next in nodeNeigbors[cur]:
                    if distance[next]==distance[cur]+1:
                        dfs(next,end,nodeNeigbors,distance,solution,res)
            del solution[len(solution)-1]
        
        dictr=set(wordList)
        res=list()
        nodeNeigbors={}
        distance={}
        solution=list()
        dictr.add(beginWord)
        bfs(beginWord,endWord,dictr,nodeNeigbors,distance)
        dfs(beginWord,endWord,nodeNeigbors,distance,solution,res)
        return res 

               
      
if __name__ =="__main__":
    c=Solution()
    print(c.findLadders("hit","cog", ["hot","dot","dog","lot","log","cog"]))


