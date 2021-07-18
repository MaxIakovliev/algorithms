class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[abs(nums[i])-1]<0:
                return abs(nums[i])
            else:
                nums[abs(nums[i])-1]*=(-1)

if __name__=="__main__":
    c=Solution()
    print("res="+str(c.findDuplicate([1,2,4,2,2,3])))
    print("res="+str(c.findDuplicate([1, 3, 2, 4, 5, 4, 6])))
