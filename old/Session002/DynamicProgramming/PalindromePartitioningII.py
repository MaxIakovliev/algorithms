class Solution:
    """
    https://leetcode.com/problems/palindrome-partitioning-ii/

    solution:
    https://leetcode.com/problems/palindrome-partitioning-ii/discuss/286262/java-4ms-dp-solution-with-explanation
    """
    def minCut(self, s: str) -> int:
        is_palindrome=[[False for i in range(len(s))] for j in range(len(s))]
        dp=[0 for i in range(len(s))]
        for i in range(len(s)):
            min_val=float('inf')
            for j in range(i+1):
                if s[i]==s[j] and (j+1>=i or is_palindrome[j+1][i-1]):
                    is_palindrome[j][i]=True
                    if j==0:
                        min_val=0
                    else:
                        min_val=min(min_val, dp[j-1]+1)
            dp[i]=min_val
        return dp[-1]
if __name__ == "__main__":
    c=Solution()
    print(c.minCut("aabbc"))#1



        