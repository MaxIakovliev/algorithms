class Solution:
    def search(self, nums, target):
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
            elif nums[mid]>target:
                hi=mid
            else:
                lo=mid+1
        return -1
if __name__=="__main__":
    c=Solution()
    print(c.search([-1,0,3,5,9,12],9))
    print(c.search([-1,0,3,5,9,12],2))
    print(c.search([-1,0,3,5,9,12],13))
    print(c.search([-1,0,3,5,9,12],9))