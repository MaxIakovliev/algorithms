class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx=0
        while (idx<len(nums)):
            if idx==0:
                idx+=1
                continue
            if nums[idx-1]==nums[idx]:
                del nums[idx]
            else:
                idx+=1
        return len(nums)