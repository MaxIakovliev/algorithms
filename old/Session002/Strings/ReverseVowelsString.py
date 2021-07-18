class Solution:
    """
    https://leetcode.com/problems/reverse-vowels-of-a-string/description/
    """
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        start=0
        end=len(s)-1
        vowels={'a', 'e','i', 'o', 'u','A', 'E','I', 'O', 'U'}
        res=[]
        idx={}
        while start<=end:
            if s[start] in vowels and s[end]in vowels:
                idx[start]=s[end]
                idx[end]=s[start]
                start+=1
                end-=1
            elif s[start]not in vowels:
                start+=1
            elif s[end] not in vowels:
                end-=1
        i=0
        while i<len(s):
            if i in idx:
                res.append(idx[i])
            else:
                res.append(s[i])
            i+=1

        return "".join(res)
if __name__=="__main__":
    c=Solution()
    print(c.reverseVowels("leetcode"))
    print(c.reverseVowels("aA"))
            

        
                    
                


        