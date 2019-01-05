class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        found=True
        maxsoFar=0
        for i in range(1, len(nums)):
            if nums[i]>nums[maxsoFar] and nums[maxsoFar]==0:
                
                maxsoFar=i            
            elif nums[i]>nums[maxsoFar] and nums[maxsoFar]!=0 and nums[i]//nums[maxsoFar]>=2:
                found=True
                maxsoFar=i
            elif nums[i]>nums[maxsoFar]:
                maxsoFar=i
                found=False
            elif nums[i]<nums[maxsoFar] and nums[i]!=0 and  nums[maxsoFar]//nums[i]<2:
                found=False

        if found:
            return maxsoFar
        return -1
