class Solution:
    """
    https://leetcode.com/problems/find-common-characters/
    """
    def commonChars(self, words: 'List[str]') -> 'List[str]':
        res=[]
        tmp=[]
        for word in words:
            d={}
            for char in word:
                if char in d:
                    d[char]+=1
                else:
                    d[char]=1
            tmp.append(d)
        first=tmp[0]
        count=0
        for k,v in first.items():
            curMin=v
            count+=1
            for i in range(1, len(tmp)):
                if k in tmp[i]:
                    curMin=min(curMin, tmp[i][k])
                    count+=1
            if count==len(tmp):
                for i in range(curMin):
                    res.append(k)
            count=0
        return res


if __name__ == "__main__":
    c=Solution()
    print(c.commonChars( ["bella","label","roller"]))#['e', 'l', 'l']
    print(c.commonChars( ["cool","lock","cook"]))#["c","o"]
            

        