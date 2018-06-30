class Solution:
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        this is accepted solution.
        """
        nums.sort()
        lo = nums[1]-nums[0]
        for i in range(1, len(nums)-1):
            lo = min(lo, nums[i+1]-nums[i])

        hi = nums[len(nums)-1]-nums[0]

        while(lo < hi):
            mid = lo+(int)((hi-lo)/2)
            if self.countPairs(nums, mid) < k:
                lo = mid+1
            else:
                hi = mid
        return lo

    def countPairs(self, nums, mid):
        res=0
        for i in range(len(nums)):
            res+=self.upperBound(nums,i, len(nums)-1,nums[i]+mid)-i-1
        return res
            
        

    def upperBound(self, nums: list, lo: int, hi: int, key: int)->(int):
        if nums[hi] <= key:
            return hi+1
        while(lo < hi):
            mid = lo+((int)((hi-lo)/2))
            if key>=nums[mid]:
                lo=mid+1
            else:
                hi=mid
        return lo



if __name__ == "__main__":
    c = Solution()
    print(c.smallestDistancePair([1, 3, 1], 1))
    print(c.smallestDistancePair([1,6,1], 3)) #expected: 5
