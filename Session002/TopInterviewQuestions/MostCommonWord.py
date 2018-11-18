class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        sban=set(banned)
        maxSoFar=0
        words=paragraph.lower().split(' ')
        punct=set("!?',;.")
        u={}
        i=0
        while i<len(words):
            if len(words[i])==0:
                i+=1
                continue
            if words[i][-1] in punct:
                curwords=words[i].replace(words[i][-1],' ').split(' ')
                words.extend(curwords)
                i+=1
                continue           

            if words[i] in punct:
                i+=1
                continue
            elif words[i] in sban:
                i+=1
                continue
            else:
                if words[i] in u:
                    u[words[i]]+=1
                else:
                    u[words[i]]=1
                maxSoFar=max(maxSoFar,u[words[i]])
            i+=1
        for k,v in u.items():
            if v==maxSoFar:
                return k
        return ""
if __name__=="__main__":
    c=Solution()
    print(c.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",['hit']))
    print(c.mostCommonWord("a.",[]))
    print(c.mostCommonWord("a, a, a, a, b,b,b,c, c",["a"]))


         