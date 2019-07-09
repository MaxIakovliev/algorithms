class Solution:
    """
    https://leetcode.com/problems/out-of-boundary-paths/

    answer:
    https://leetcode.com/problems/out-of-boundary-paths/discuss/112337/Straightforward-Python-DP-Solution
    """
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        def helper(N, i, j):
            if(N, i, j) in self.memo:
                return self.memo[(N, i, j)]
            if N == 0:
                return 0
            ans = 0
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if i+x >= 0 and i+x < m and j+y >= 0 and j+y < n:
                    ans += helper(N-1, i+x, j+y)
                else:
                    ans += 1
            self.memo[(N, i, j)] = ans
            return ans

        self.memo = {}
        return helper(N, i, j) % (10**9+7)

        
