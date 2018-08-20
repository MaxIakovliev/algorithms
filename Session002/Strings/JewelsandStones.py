class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        u=set(J)
        res=0
        for c in S:
            if c in u:
                res+=1
        return res