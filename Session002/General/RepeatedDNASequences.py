class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        u={}
        for i in range(len(s)-9):
            tmp=s[i:i+10]
            if tmp in u:
                u[tmp]+=1
            else:
                u[tmp]=1
        res=[]
        for k,v in u.items():
            if v>1:
                res.append(k)
        return res
if __name__=="__main__":
    c=Solution()
    print(c.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
    print(c.findRepeatedDnaSequences("AAAAAAAAAAA"))