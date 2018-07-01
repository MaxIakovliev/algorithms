class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo=0
        hi=len(nums)-1

        while lo<=hi:
            mid =(int)((lo+hi)/2)
            if nums[mid]==target:
                return mid
            elif nums[mid]<target and mid+1<len(nums) and nums[mid+1]>target :
                return mid+1
            elif nums[mid]<target and mid==len(nums)-1:
                return mid+1
            elif nums[mid]<target:
                lo=mid+1
            elif nums[mid]>target and mid==0:
                return 0
            elif nums[mid]>target:
                hi=mid
                
            
                    

                


if __name__ =="__main__":
    c=Solution()
    print(c.searchInsert([1,3,5,6],5))
    print(c.searchInsert([1,3,5,6],2))
    print(c.searchInsert([1,3,5,6],0))
    print(c.searchInsert([1,3,5,6],8))
    print(c.searchInsert([1,3,5,6],6))