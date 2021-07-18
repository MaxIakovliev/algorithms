class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo=0
        hi=len(nums)-1
        while lo!=hi:
            mid=(lo+hi)//2
            if nums[mid]>nums[mid+1]:
                hi=mid
            else:
                lo=mid+1
        return lo


if __name__ =="__main__":
    c=Solution()
    print(c.findPeakElement([1,2,3,1]))
    print(c.findPeakElement([1,2,1,3,5,6,4]))
            