class Solution:
    """
    https://leetcode.com/problems/maximum-gap/
    """
    def maximumGap(self, nums: 'List[int]') -> 'int':
        if len(nums)<2:
            return 0
        
        nums.sort()

        maxSoFar=float('-inf')
        for i in range(1,len(nums)):
            maxSoFar=max(maxSoFar, nums[i]-nums[i-1])
        return maxSoFar