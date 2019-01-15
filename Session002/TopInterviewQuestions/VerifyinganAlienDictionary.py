class Solution:
    """
    https://leetcode.com/problems/verifying-an-alien-dictionary/description/
    """
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        d={}
        for i in range(len(order)):
            d[order[i]]=i
        maxLenSoFar=0
        for word in words:
            maxLenSoFar=max(maxLenSoFar,len(word))
        
        for i in range(len(words)-1):
            cur=words[i]
            nxt=words[i+1]
            ln=max(len(cur), len(nxt))
            for j in range(ln):
                if j>=len(nxt):
                    return False 
                if j>=len(cur):
                    break              
                if cur[j]!=nxt[j]:
                    if d[cur[j]]<d[nxt[j]]:
                        break
                    else:
                        return False
                else:
                    continue
        return True


    def isAlienSorted2(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        d={}
        for i in range(len(order)):
            d[order[i]]=i
        maxSize=0
        for i in range(len(words)):
            maxSize=max(maxSize, len(words[i]))

        for i in range(len(words)-1):
            cur=words[i]
            nxt=words[i+1]
            ln=max(len(cur),len(nxt))
            for j in range(ln):
                if j>=len(nxt):
                    return False

                if j>=len(cur):
                    break
                if cur[j]!=nxt[j]:
                    if d[cur[j]]<d[nxt[j]]:
                        break
                    else:
                        return False
                else:
                    continue
        return True




    def isAlienSorted3(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        d={}
        for i in range(len(order)):
            d[order[i]]=i
        
        for i in range(len(words)-1):
            cur=words[i]
            nxt=words[i+1]
            ln=max(len(cur),len(nxt))
            for j in range(ln):
                if j>=len(nxt):
                    return False
                if j>=len(cur):
                    break
                if cur[j]!=nxt[j]:
                    if d[cur[j]]<d[nxt[j]]:
                        break
                    else:
                        return False
                else:
                    continue
        return True
        
       



        


if __name__=="__main__":
    c=Solution()
    print(c.isAlienSorted(["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz"))
    print(c.isAlienSorted(["word","world","row"],"worldabcefghijkmnpqstuvxyz"))
    print(c.isAlienSorted(["apple","app"],"abcdefghijklmnopqrstuvwxyz"))




            
        