class Solution:
    """
    https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
    """
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return float('inf')
        if len(nums)==1:
            return nums[0]
        elif nums[0]<nums[-1]:
            return nums[0]
        else:
            return min(self.findMin(nums[len(nums)//2:]), self.findMin(nums[:len(nums)//2]))
        