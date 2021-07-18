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


    def rob2(self, nums):  # Recursive (top-down)
        def do_rob(arr, idx):
            if idx<0:
                return 0
            return max(do_rob(arr, idx-2)+arr[idx], do_rob(arr, idx-1))
            
        do_rob(nums, len(nums)-1)


    def rob3(self, nums):  # Recursive + memo (top-down).
        self.memo=[-1 for i in range(len(nums)+1)]
        def do_rob(arr,idx):
            if idx<0:
                return 0
            if self.memo[idx]>=0:
                return self.memo[idx]
            res=max(do_rob(arr,idx-2)+arr[idx], do_rob(arr,idx-1))
            self.memo[idx]=res
            return res
        
        do_rob(nums,len(nums)-1)



if __name__ == "__main__":
    c = Solution()
    print(c.rob([1,2,3,1]))
    print(c.rob([2,1,1,2]))