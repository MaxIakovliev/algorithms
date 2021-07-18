class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo=0
        hi=len(nums)
        while lo<hi:
            mid=(int)((lo+hi)/2)
            if nums[mid]==target:
                return mid
            elif nums[mid]<target and mid+1<len(nums) and nums[mid+1]>target:
                return mid+1
            elif nums[mid]<target:
                lo=mid+1
            elif nums[mid]>target:
                hi=mid
        if hi==0:
            return 0
        if lo>=len(nums):
            return len(nums)


if __name__ =="__main__":
    c=Solution()
    print(c.searchInsert([1,3,5,6], 5)) #2
    print(c.searchInsert([1,3,5,6], -1)) #0
    print(c.searchInsert([1,3,5,6], 10)) #4
    print(c.searchInsert([1,3,5,6], 2)) #1
    print(c.searchInsert([1,3,5,6], 7)) #4
    print(c.searchInsert([1,3,5,6], 0)) #0