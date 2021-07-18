class Solution:
    """
    https://leetcode.com/problems/convert-to-base-2/
    """
    def baseNeg2(self, N: int) -> str:
        if N==0 or N==1: return str(N)
        return self.baseNeg2(-(N>>1))+str(N&1)