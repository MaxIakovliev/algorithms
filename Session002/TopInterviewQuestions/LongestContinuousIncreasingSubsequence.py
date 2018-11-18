class Solution(object):
    """
    https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
    """
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSoFar=0
        count=0
        for i in range(len(nums)):
            if i==0:
                count=1
            else:
                if nums[i]>nums[i-1]:
                    count+=1
                else:
                    count=1
        
            maxSoFar=max(maxSoFar,count)
        return maxSoFar
        