class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''

        maxLen=0
        idx=0
        i=0
        chr=strs[0][idx]
        while i< len(strs):
            if idx>len(strs[i])-1 or strs[i][idx]!=chr:
                break
            i+=1
            
            if i==len(strs):               
                idx+=1
                maxLen+=1
                if idx>len(strs[0])-1:
                    break
                chr=strs[0][idx]
                
                i=0
        if maxLen==0:
            return ''
        return strs[0][0:maxLen]

if __name__ =='__main__':
    c=Solution()
    res=c.longestCommonPrefix(["fl","fl","fl"])
    print(res)

    res=c.longestCommonPrefix(["flw","flw","fl"])
    print(res)
                
    res=c.longestCommonPrefix(["fl0w","","fl0"])
    print(res)

    res=c.longestCommonPrefix(["cab","ab","ab"])
    print(res)
        
