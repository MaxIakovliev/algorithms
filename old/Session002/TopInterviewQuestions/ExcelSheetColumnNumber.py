class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        for c in s:
            res*=26
            res+=ord(c)-ord('A')+1
        return res

if __name__ =="__main__":
    c=Solution()
    print(c.titleToNumber('A')) #1
    print(c.titleToNumber('AB')) #28
    print(c.titleToNumber('ZY')) #701