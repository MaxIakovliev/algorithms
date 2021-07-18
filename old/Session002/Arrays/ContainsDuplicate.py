class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<=1:
            return False
        
        nums.sort()
        start=0
        end=len(nums)-1
        while start<end:
            if nums[start]==nums[end]:
                return True
            if start>0 and nums[start]==nums[start-1]:
                return True
            if end<len(nums)-1 and nums[end]==nums[end+1]:
                return True
            
            start+=1
            end-=1
        return False

if __name__=="__main__":
    c=Solution()
    print(c.containsDuplicate([1,1,2,3])) #true
    print(c.containsDuplicate([1,2,3,3])) #true
    print(c.containsDuplicate([1,2,2,3])) #true
    print(c.containsDuplicate([1,2,3,4])) #false