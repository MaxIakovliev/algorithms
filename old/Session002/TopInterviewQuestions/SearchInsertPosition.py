class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return -1
        lo=0
        hi=len(nums)-1
        while lo<=hi:
            mid=(lo+hi)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                if mid==0:
                    return 0
                if nums[mid-1]<target:
                    return mid
                else:
                    hi=mid-1
            else:
                if mid==len(nums)-1:
                    return mid+1
                if nums[mid+1]>target:
                    return mid+1
                else:
                    lo=mid+1
        return -1

if __name__=="__main__":
    c=Solution()
    print(c.searchInsert([1,3,5,6], 5))
    print(c.searchInsert([1,3,5,6], 2))
    print(c.searchInsert( [1,3,5,6], 7))
    print(c.searchInsert([1,3,5,6], 0))
        