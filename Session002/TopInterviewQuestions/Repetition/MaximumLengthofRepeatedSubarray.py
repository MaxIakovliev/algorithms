class Solution(object):
    """
    https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
    """
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        решается  методом динамического программирования
        """
        res=[0]*(len(B)+1)
        maxSoFar=float('-inf')
        for i in range(len(A)):
            tmp=[0]*(len(B)+1)
            for j in range(len(B)):
                if A[i]==B[j]:
                    tmp[j+1]=1+res[j]
                maxSoFar=max(maxSoFar,tmp[j+1])
            res=tmp
        return maxSoFar
if __name__=="__main__":
    c=Solution()
    print(c.findLength([1,2,3,2,1],[3,2,1,4,7]))
                