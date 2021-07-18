class Solution(object):
    """
https://leetcode.com/problems/number-of-1-bits/description/
    """
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<0:
            return 0
        count=0
        while n>0:
            if n&1==1:
                count+=1
            n=n>>1
        return count
if __name__=="__main__":
    c=Solution()
    print(c.hammingWeight(128))#1
    print(c.hammingWeight(11))#3
        