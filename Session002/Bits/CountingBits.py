class Solution:
    """
    https://leetcode.com/problems/counting-bits/submissions/
    """
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        def calc(n):
            res=0
            while n!=0:
                n&=n-1
                res+=1
            return res
        res=[]
        for i in range(num+1):
            res.append(calc(i))
        return res


        