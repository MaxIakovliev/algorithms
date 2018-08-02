class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        for i in range(len(nums)):
            if i==1:
                nums[i]=max(nums[0],nums[1])
            if i>1:
                nums[i]=max(nums[i]+nums[i-2], nums[i-1])
        return max(nums)



if __name__ == "__main__":
    c = Solution()
    print(c.rob([1,2,3,1]))
    print(c.rob([2,1,1,2]))