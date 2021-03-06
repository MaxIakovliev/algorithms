class Solution:
    """
    https://leetcode.com/problems/ones-and-zeroes/

In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:

    The given numbers of 0s and 1s will both not exceed 100
    The size of given string array won't exceed 600.

 

Example 1:

Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”

 

Example 2:

Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".



    
    solution:
    https://leetcode.com/problems/ones-and-zeroes/discuss/228831/Python-DP
    """
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp=[[0 for i in range(n+1)] for j in range(m+1)]
        for str in strs:
            zeros=0
            ones=0
            for char in str:
                if char=='0':
                    zeros+=1
                elif char=='1':
                    ones+=1

            for i in range(m, zeros-1,-1):
                for j in range(n, ones-1,-1):
                    dp[i][j]=max(dp[i][j],dp[i-zeros][j-ones]+1)
        return dp[m][n]

        