class Solution:
    def twoSum(self, nums, target):
        if len(nums) < 2:
            return []
        temp = {}
        for indx, value in enumerate(nums):
            diff = target-value
            if diff in temp:
                return [temp[diff], indx]
            else:
                temp[value] = indx
