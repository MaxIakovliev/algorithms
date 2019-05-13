class Solution:
    """
    https://leetcode.com/problems/minimum-cost-for-tickets/
    solution:
    https://leetcode.com/problems/minimum-cost-for-tickets/discuss/227236/Python-solution
    """
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> int:
        dp=[0]*366
        j=0
        for i in range(days[0],366):
            if i==days[j]:
                dp[i]=dp[i-1]+costs[0]
                if i>=7:
                    dp[i]=min(dp[i],dp[i-7]+costs[1])
                else:
                    dp[i]=min(dp[i],costs[1])
                
                if i>=30:
                    dp[i]=min(dp[i],dp[i-30]+costs[2])
                else:
                    dp[i]=min(dp[i],costs[2])
                j+=1
                if j==len(days):
                    return dp[i]
            else:
                if i>0:
                    dp[i]=dp[i-1]


if __name__ == "__main__":
    c=Solution()
    print(c.mincostTickets([1,4,6,7,8,20],[2,7,15]))



        