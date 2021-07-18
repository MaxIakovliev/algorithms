class Solution:
    """
    https://leetcode.com/problems/combination-sum-iv/
    solution:
    https://leetcode.com/problems/combination-sum-iv/discuss/294990/Python-DP-beats-97-speed-and-91-memory-(with-explanation)
    """
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[0]*(target+1)
        for num in nums:
            if num<=target:
                dp[num]=1
        for i in range(target+1):
            for num in nums:
                if i-num>0:
                    dp[i]+=dp[i-num]
        return dp[-1]
        