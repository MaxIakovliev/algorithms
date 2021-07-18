class Solution:
    """
    https://leetcode.com/problems/score-after-flipping-matrix/
    solution:
    1. https://leetcode.com/problems/score-after-flipping-matrix/discuss/143812/C%2B%2BJava-From-Intuition-Un-optimized-code-to-Optimized-Code-with-Detailed-Explanation
    
    """
    def matrixScore(self, a: 'List[List[int]]') -> int:
        m=len(a)
        n=len(a[0])
        res=0
        res+=(1<<(n-1))*m
        for j in range(1,n):
            same=0
            for i in range(m):
                if a[i][0]==a[i][j]:
                    same+=1
            res+=(1<<(n-1-j))*max(same, m-same)
        return res        