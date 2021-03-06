class Solution:
    
    def smallestDistancePair3(self, nums, k):
        """
        
    2 <= len(nums) <= 10000.
    0 <= nums[i] < 1000000.
    1 <= k <= len(nums) * (len(nums) - 1) / 2.

        """
        nums.sort()
        distance=[0]*(nums[len(nums)-1]+1) #based on provided input information
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                distance[abs(nums[i]-nums[j])]+=1

        idx=0
        n=len(distance)
        for i in range(n):
            count=distance[i]
            for j in range(count):
                idx+=1
                if idx==k:
                    return i

        return 0
            




    def smallestDistancePair2(self, nums, k):
        """
        accepted solution
        150ms
        beats 40.7% of solutions
        """
        nums.sort()
        lo=nums[1]-nums[0]
        n=len(nums)
        for i in range(1,n-1):
            lo=min(lo, nums[i+1]-nums[i])
        
        hi=nums[n-1]-nums[0]
        while(lo+1<hi):
            # mid= lo+((int)((hi-lo)/2))
            mid=(int)((lo+hi)/2)
            count=self.countLessThan(nums, mid)
            if count>self.countLessThan(nums,mid+1) and count==k:
                return mid
            if count<k:
                lo=mid
            else:
                hi=mid
        if self.countLessThan(nums, lo)>=k:
            return lo
        return hi

    def countLessThan(self, nums:list, k:int)->(int):
        right=0
        count=0
        n=len(nums)
        for i in range(n):
            while(nums[i]-nums[right]>k and right<=i):
                right+=1
            count+=(i-right)
        return count
            
    



    #---------------------------------
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        this is accepted solution.
        700ms
        beat 6.98% of other solutions
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
    print(c.smallestDistancePair3([1, 3, 1], 1))
    print(c.smallestDistancePair3([1,6,1], 3)) #expected: 5
    print(c.smallestDistancePair3([62,100,4],2)) #expected: 58
    print(c.smallestDistancePair3([1,2,0,2,1,0,1,1,0,2,2,0,2,0,1,1,1,0,1,0,1,1,2,2,2,2,0,0,2,1,2,1,2,0,0,0,1,0,0,1,0,2,1,1,1,1,0,2,2,1,0,2,0,2,2,2,1,0,2,2,2,2,0,0,1,0,1,1,2,1,2,2,1,1,0,2,0,1,0,1,1,2,0,1,1,1,1,2,0,2,2,0,0,1,1,1,1,2,1,2,2,1,2,0,1,2,2,1,1,2,1,0,1,1,1,0,0,1,2,0,2,1,0,1,2,0,2,2,1,0,0,2,0,1,1,0,1,0,1,0,1,2,2,2,0,1,1,1,1,1,0,2,2,2,1,0,1,0,1,0,0,0,0,2,0,0,1,1,2,0,2,1,2,0,0,1,0,1,2,1,0,1,1,1,1,0,0,2,2,1,1,0,0,0,0,1,2,2,1,1,0,1,2,0,0,2,1,2,1,2,0,2,1,1,2,2,2,2,2,0,1,1,0,1,2,2,0,2,2,2,0,2,0,1,1,2,2,0,2,2,2,2,2,2,1,0,2,2,2,0,2,0,2,0,2,1,0,1,0,1,1,0,2,0,1,0,0,2,0,0,0,2,0,2,2,0,2,0,0,1,1,0,2,0,1,2,2,0,1,1,2,0,0,0,2,1,0,1,0,2,1,2,0,1,2,1,1,1,0,1,2,1,2,2,1,2,0,2,1,0,1,1,1,2,0,2,2,2,2,1,0,2,2,1,1,1,1,0,1,2,2,0,1,2,2,1,0,0,1,2,1,0,2,1,1,1,0,0,0,1,1,1,0,2,0,2,0,1,2,2,0,2,1,2,2,0,0,0,0,2,1,1,2,0,2,0,1,0,1,0,2,0,0,0,2,1,2,0,1,2,1,2,1,0,1,0,1,0,0,1,2,1,1,2,1,1,2,2,1,0,1,1,2,2,1,2,2,2,1,0,1,1,1,0,0,0,2,1,1,1,2,2,1,2,0,2,1,2,0,2,2,2,1,1,2,2,0,0,2,2,2,1,2,2,1,0,2,0,2,0,2,1,2,2,1,1,1,1,1,0,0,1,0,2,2,0,0,2,1,0,1,0,2,1,0,0,0,0,1,2,1,2,0,0,1,1,2,2,2,2,0,2,1,0,0,0,2,0,1,1,0,2,1,1,1,2,1,0,0,1,0,1,0,1,2,0,2,1,0,0,1,2,1,1,0,0,0,2,2,2,1,1,2,2,0,1,0,2,2,2,0,1,0,0,1,0,0,1,1,1,1,1,1,2,1,2,0,2,0,2,1,2,2,2,0,1,0,1,2,0,2,2,1,2,0,1,2,2,0,1,1,0,1,1,0,0,0,1,2,1,0,0,2,0,1,0,2,2,0,1,0,0,0,1,0,0,0,2,1,1,1,1,1,0,1,1,0,1,0,1,0,2,2,0,2,2,0,0,1,2,0,1,1,1,2,0,0,0,2,0,2,2,2,2,1,0,2,2,0,0,1,1,2,2,2,1,1,2,0,1,0,0,1,0,1,2,0,1,2,0,1,1,1,1,2,0,1,0,1,2,2,0,0,2,0,1,2,1,2,1,0,0,1,0,0,1,2,0,1,0,0,0,0,2,0,1,0,1,2,0,1,2,0,0,0,0,1,1,2,0,0,0,2,1,1,0,0,2,2,1,0,0,1,0,1,0,1,1,0,2,0,1,1,2,2,1,1,0,2,0,0,1,0,1,2,2,1,2,2,2,2,2,1,2,0,0,0,1,1,0,0,2,1,0,1,0,2,2,0,1,2,2,2,0,0,0,2,2,1,2,1,0,0,0,1,1,2,1,2,0,1,2,1,0,1,2,0,1,2,1,2,1,1,1,2,2,1,0,1,0,2,1,2,0,2,0,0,0,1,2,1,0,0,0,1,2,0,2,2,2,1,0,2,2,1,1,2,0,0,1,2,2,2,1,2,1,2,1,0,2,2,0,0,0,2,0,1,0,1,0,2,2,2,2,0,1,1,1,1,0,1,0,0,1,2,0,1,0,0,2,0,1,1,1,1,2,0,1,1,2,0,2,1,2,1,1,0,1,1,2,1,2,0,1,0,0,0,1,0,2,0,0,2,0,0,1,0,1,2,2,1,2,0,2,2,2,0,2,0,2,1,0,0,0,0,0,0,1,0,2,0,1,1,0,2,1,2,1,1,0,2,1,2,0,1,1,1,0,1,0,1,0,0,1,1,0,1,1,0,2,2,1,1,0,1,0,0,0,2,2,2,0,1,2,1,2,0,2,1,0,0,1,2,2,1,0,1,2,0,0,2,1,1,2,0,0,1,0,2,2,2,2,0,1,0,0,0,1,1,0,2,0,2,0,2,2,2,0,2,0,0,2,1,0,2,2,2,1,2,0,2,2,0,2,1,2,2,0,1,0,2,0,1,1,2,2,2,2,0,0,0,0,2,2,2,2,1,0,2,0,2,0,1,0,1,1,2,2,1,2,1,2,0,1,2,2,2,0,1,0,1,0,1,0,1,0,1,2,2,0,2,2,2,0,1,0,2,1,1,1,0,0,0,0,0,2,0,1,0,2,0,0,2,2,2,2,1,2,2,1,2,0,1,0,1,1,0,0,2,2,1,2,2,1,0,0,0,0,0,0,1,1,0,1,0,2,0,1,0,2,2,2,0,1,0,2,1,2,2,0,2,1,1,1,1,1,1,2,2,1,0,1,2,1,1,0,0,1,0,2,0,2,2,2,2,1,2,2,2,2,1,2,2,1,1,1,0,1,2,2,0,0,2,1,0,2,1,0,2,2,0,2,1,0,2,1,0,0,0,0,2,0,1,0,2,0,1,2,2,0,1,0,1,1,1,2,1,0,0,0,0,0,2,0,1,1,1,0,1,2,2,1,2,2,0,2,2,0,0,0,2,2,2,1,1,2,1,2,1,2,1,1,0,0,2,0,2,0,1,1,0,0,2,1,0,0,1,2,0,1,0,2,1,1,1,1,2,2,0,2,2,0,1,1,2,2,0,2,0,1,0,2,0,2,2,2,1,2,2,0,1,1,2,2,1,2,2,2,2,2,2,0,0,1,1,0,0,1,0,0,0,2,1,2,1,2,2,1,1,0,2,1,0,0,1,2,2,1,1,1,1,0,0,0,2,0,0,2,1,1,2,2,2,1,2,1,0,1,2,1,2,2,1,1,0,0,0,1,1,1,0,0,1,1,1,2,2,1,2,1,0,2,0,1,0,0,2,0,0,0,2,1,0,2,0,2,1,1,2,0,1,1,0,2,0,1,2,2,0,0,2,0,1,1,0,2,2,1,0,0,0,2,0,1,0,0,0,2,0,2,2,1,0,1,2,2,2,2,1,1,2,2,2,0,1,2,0,2,1,2,1,0,2,0,1,0,0,2,1,0,0,0,2,0,0,1,2,2,0,0,1,0,1,1,2,2,2,0,2,1,0,2,0,1,2,1,0,1,1,1,2,1,0,0,0,2,1,0,2,2,0,1,0,2,0,2,2,2,0,1,2,2,2,1,0,0,1,0,0,0,1,1,0,1,2,2,2,0,1,0,0,1,2,2,2,0,1,1,1,2,0,2,1,1,2,2,1,0,1,2,0,2,1,1,0,1,1,2,0,1,0,2,1,2,0,2,2,2,2,0,2,0,2,1,0,1,0,2,1,0,0,0,2,0,0,0,1,0,2,1,0,0,0,0,0,2,1,0,0,0,2,1,2,0,0,0,2,2,2,2,1,1,1,0,1,2,2,0,0,1,1,0,2,0,2,1,2,0,0,2,1,0,0,0,2,2,0,1,1,0,0,0,0,1,0,1,1,2,1,2,1,2,0,1,1,2,0,0,2,1,0,0,2,0,1,2,1,1,2,2,2,1,2,2,0,1,2,0,1,2,1,2,0,2,1,0,2,1,1,2,0,2,0,1,2,2,1,2,1,1,1,1,2,1,2,1,2,0,1,1,1,2,0,1,2,1,1,0,2,1,0,2,0,0,0,2,1,0,1,2,0,1,0,1,1,0,0,1,0,2,0,0,0,0,2,2,0,1,1,2,1,2,2,1,0,1,1,2,2,0,1,0,1,0,2,1,0,2,0,2,2,1,1,1,1,2,2,2,2,0,1,1,0,2,0,1,2,1,2,0,0,2,2,1,2,2,1,1,0,0,0,0,2,1,0,2,2,0,1,2,2,2,1,1,2,2,2,2,2,2,2,2,2,0,0,1,2,2,0,2,0,1,2,2,1,0,2,2,0,0,0,2,0,0,0,1,2,1,0,2,2,1,2,0,0,2,2,2,1,1,1,2,0,0,2,0,0,2,1,2,2,2,1,0,0,1,1,1,0,0,2,0,1,1,0,0,0,1,0,2,0,0,1,1,2,0,2,0,2,0,1,0,0,1,1,0,1,0,1,1,0,2,1,0,1,0,1,2,0,0,1,2,0,2,1,0,1,1,2,0,2,2,1,1,2,2,1,1,0,2,2,2,2,1,2,0,2,0,2,2,1,1,0,1,0,0,1,2,2,1,1,1,0,1,0,1,2,0,2,1,2,2,0,2,2,0,1,1,0,0,1,1,1,1,1,0,1,2,0,2,2,0,1,2,2,1,1,2,0,1,1,1,2,0,2,1,1,2,1,1,1,1,2,1,0,1,2,0,1,1,1,0,2,1,2,0,0,2,1,0,1,0,2,2,2,1,1,1,2,2,0,2,1,0,2,2,2,2,2,2,0,0,1,2,2,2,0,0,2,0,2,2,2,2,2,2,2,0,2,1,1,2,0,2,2,0,2,1,0,0,1,1,1,1,2,1,2,0,2,0,0,0,2,2,0,0,2,1,2,1,0,1,0,2,0,1,2,0,1,2,0,1,1,1,1,0,2,2,1,0,2,1,0,2,0,1,0,0,2,1,0,1,0,2,2,2,1,2,2,0,2,1,0,2,0,2,1,1,2,0,1,2,0,0,1,1,1,0,2,0,0,2,2,0,0,2,2,1,0,1,2,1,1,2,1,0,0,1,0,0,0,0,0,1,2,2,2,1,1,2,0,1,2,1,2,1,1,1,1,1,0,2,1,1,1,0,2,0,0,0,2,1,0,1,2,0,1,1,2,1,1,2,2,0,2,0,2,0,2,0,2,2,0,0,1,0,2,0,0,0,0,0,1,0,2,1,1,0,1,2,2,1,0,2,2,1,2,0,1,2,2,2,0,1,0,0,1,0,2,1,0,1,1,1,1,2,1,2,0,1,2,2,2,2,2,0,1,0,2,2,0,0,0,0,1,2,1,1,1,1,0,1,0,0,0,0,2,2,2,0,0,0,1,2,2,2,2,2,2,2,1,2,1,1,1,2,0,1,1,2,0,0,1,2,0,2,0,2,2,1,2,2,2,2,2,1,1,2,1,1,1,2,0,1,2,2,1,1,0,2,1,2,1,1,1,0,2,1,0,0,2,2,2,1,0,1,2,1,2,1,1,0,0,0,2,1,0,1,0,0,1,2,0,0,2,0,0,0,1,0,1,0,1,0,1,0,1,1,1,0,2,2,0,0,0,1,2,0,1,1,1,1,2,1,1,0,1,1,1,0,1,1,2,1,2,2,1,2,2,2,1,1,0,2,1,0,2,0,1,1,0,1,2,1,1,0,2,0,0,1,0,0,1,0,0,1,2,2,0,1,2,1,2,2,2,2,0,2,1,1,0,0,0,1,1,2,2,0,0,0,1,2,0,1,2,0,1,2,1,1,2,1,2,2,0,1,2,2,1,2,0,1,1,0,0,0,0,1,2,2,2,0,1,0,1,0,2,1,1,0,2,1,2,1,2,0,2,0,0,1,2,0,1,0,0,0,1,1,1,2,1,1,1,0,1,2,0,0,0,1,0,2,0,2,0,1,1,1,0,0,0,2,0,1,2,0,1,0,1,1,0,1,0,1,1,2,1,1,2,2,1,1,1,0,1,0,1,1,2,1,2,2,1,1,2,2,2,1,1,1,1,1,1,2,1,1,0,2,1,0,0,1,1,1,0,2,2,0,0,1,1,2,2,1,2,2,2,0,0,2,2,2,0,1,0,2,1,0,0,2,0,0,1,2,1,2,1,2,0,0,1,0,2,0,0,2,0,1,1,2,2,0,1,0,1,1,1,2,2,1,1,1,2,0,1,2,0,1,1,1,0,1,0,2,2,0,2,1,0,0,1,2,0,0,1,0,1,0,2,2,1,0,1,2,2,0,2,2,0,0,1,1,1,2,1,2,2,2,0,1,0,0,0,1,0,0,0,1,1,0,2,1,0,2,1,2,0,2,0,2,2,0,2,2,0,1,0,0,2,0,2,2,1,0,2,0,2,2,1,1,2,2,2,1,0,0,1,2,1,0,1,0,2,2,1,2,1,2,0,1,0,1,2,2,1,0,2,0,2,1,0,1,2,0,0,2,2,1,1,0,0,1,2,0,2,2,1,2,1,0,1,1,0,0,2,2,2,2,2,0,1,0,1,1,1,0,1,2,1,0,2,2,0,1,1,2,0,2,2,0,2,1,1,2,2,2,1,1,0,1,0,2,2,2,2,0,2,2,1,0,0,1,1,0,1,2,1,0,0,0,2,2,0,2,0,1,2,2,1,1,1,2,0,2,0,0,1,2,0,1,1,0,1,1,1,2,0,0,0,2,1,0,2,1,2,1,0,1,1,2,2,0,1,0,2,2,2,1,1,0,1,2,1,2,0,0,0,0,1,1,1,1,0,2,1,0,0,2,0,2,0,1,1,0,0,1,2,0,2,2,2,1,1,0,0,0,0,1,0,1,2,2,2,0,1,0,1,1,0,0,1,0,0,1,1,2,2,0,0,2,2,0,0,0,2,2,2,2,1,1,2,2,2,0,0,2,0,1,2,2,2,2,0,0,2,0,2,2,2,0,2,1,1,1,1,0,2,0,2,0,0,1,2,2,1,0,2,0,1,2,2,1,2,0,0,2,0,0,1,1,1,0,2,0,2,2,2,2,1,2,2,0,1,2,2,2,0,0,0,1,0,1,2,0,0,0,0,1,2,0,0,2,2,0,1,1,2,2,2,2,0,0,0,1,0,1,0,1,1,0,0,0,2,2,0,0,1,1,0,2,2,1,1,0,2,0,2,1,0,1,2,1,1,2,1,0,0,1,2,1,1,2,2,0,1,2,0,0,0,1,1,2,0,2,1,2,0,1,0,0,0,2,0,1,1,2,2,2,0,0,0,2,2,1,0,2,1,0,0,2,1,1,2,0,2,0,2,0,1,2,2,0,0,0,2,2,1,1,1,0,0,1,1,0,0,0,2,1,1,0,1,0,2,0,1,0,2,0,2,1,0,1,2,0,0,2,1,1,0,0,1,0,2,1,1,1,2,1,2,2,0,2,2,1,2,2,2,1,0,1,1,1,2,1,1,1,1,0,0,1,1,0,2,2,0,1,1,1,1,2,1,1,0,0,2,2,0,2,1,1,1,1,2,0,2,2,2,0,1,0,1,0,0,1,0,2,0,0,0,2,1,1,2,2,0,1,1,0,0,1,0,2,0,2,2,0,2,2,0,0,1,2,0,1,0,0,0,0,1,2,0,1,1,0,0,2,0,0,2,0,1,1,2,2,1,0,1,0,0,2,2,2,0,0,1,0,2,0,1,2,1,0,1,1,2,2,2,2,0,0,0,2,1,1,2,0,1,1,1,0,0,0,1,0,2,0,2,0,2,0,0,1,0,0,2,0,2,2,2,2,2,1,0,2,0,0,0,0,0,0,2,0,2,0,1,0,2,2,2,1,1,1,0,1,0,1,1,0,2,0,0,1,2,2,1,2,0,0,0,2,2,0,1,1,0,2,0,1,2,1,0,0,0,1,1,1,2,0,1,1,1,2,1,0,2,1,0,1,0,1,2,0,1,2,0,2,0,0,0,2,0,2,2,2,0,1,1,2,0,0,1,1,0,1,1,0,2,0,1,1,2,2,1,0,2,1,2,0,0,0,2,2,2,0,1,1,0,0,1,1,1,1,0,0,2,0,2,2,0,1,0,0,1,1,1,1,1,0,0,2,0,0,2,0,2,2,2,2,1,1,1,2,0,2,1,1,0,0,1,2,1,2,2,2,2,0,0,0,1,1,0,1,0,1,1,1,2,0,2,2,2,0,1,0,1,2,2,0,0,2,0,0,1,0,0,1,2,1,0,1,2,2,1,2,2,1,1,0,2,1,0,1,1,2,1,2,1,0,2,0,1,1,0,0,1,0,2,1,1,1,2,1,0,2,2,1,2,2,1,2,2,2,2,1,1,2,1,0,0,2,2,1,1,2,1,1,1,0,0,0,0,0,0,2,2,1,0,1,0,1,1,2,2,0,1,1,2,2,1,0,2,1,1,1,2,1,2,0,0,2,0,2,0,0,0,0,2,2,2,0,0,0,2,0,2,1,0,2,1,1,0,1,0,0,2,2,1,1,2,0,0,0,1,1,1,1,1,0,2,2,2,2,1,0,0,0,1,0,1,1,0,1,2,2,1,0,1,1,0,2,0,2,2,1,1,1,1,0,0,2,2,1,2,0,0,2,1,0,2,1,2,1,2,1,0,2,2,2,0,0,1,1,0,0,1,1,1,1,2,2,2,1,0,2,0,2,2,2,1,1,1,0,0,1,1,0,1,0,0,2,1,2,0,0,0,1,2,0,1,2,0,1,0,0,0,1,0,1,2,2,1,2,0,1,0,2,1,0,1,2,1,1,1,2,1,0,0,2,1,1,1,0,2,1,2,2,2,2,2,1,1,2,1,2,1,0,1,1,0,1,2,0,1,2,2,2,2,2,1,0,2,2,2,2,0,1,2,1,2,0,0,2,0,0,0,0,0,0,2,0,0,2,0,2,1,1,2,0,1,1,2,0,0,2,2,0,0,2,0,2,2,1,0,1,0,2,0,0,0,0,2,0,1,2,1,0,1,2,0,2,0,2,1,0,0,0,1,2,0,1,1,2,1,1,1,0,0,0,0,0,2,2,0,2,2,2,1,2,1,1,1,2,0,2,1,0,0,0,2,2,1,0,2,0,2,0,1,0,1,0,2,0,1,1,1,1,0,2,0,1,2,1,2,0,2,1,2,1,2,2,2,2,1,2,0,0,2,0,2,2,2,0,1,2,1,0,2,0,2,2,2,0,1,1,0,2,2,2,2,0,1,2,1,2,2,1,2,0,1,2,0,0,0,2,2,1,1,0,0,2,1,1,1,0,1,2,0,1,2,0,0,1,2,0,2,0,0,2,0,2,0,1,1,1,1,1,0,2,1,1,2,2,0,0,1,2,1,2,2,1,0,2,2,2,2,2,0,1,0,0,1,1,2,0,1,2,1,2,0,0,0,2,2,2,1,2,1,1,2,0,0,0,0,1,1,1,0,1,0,2,0,1,1,2,2,0,0,1,2,0,2,2,1,2,0,0,1,0,1,2,2,0,1,2,1,2,1,2,1,2,0,1,1,1,1,1,2,0,2,2,1,2,2,1,1,0,0,1,0,2,0,1,1,1,1,2,2,0,0,1,0,1,0,2,2,2,1,0,2,2,2,0,0,2,2,1,2,2,0,2,0,2,1,0,2,0,0,1,1,1,0,2,0,0,0,1,0,2,1,2,1,2,1,0,1,2,0,2,0,1,2,2,1,0,1,2,1,2,1,0,2,2,2,1,1,1,0,0,1,1,1,1,1,1,2,1,1,1,0,0,2,0,1,2,2,0,1,2,2,2,2,0,2,1,1,2,2,2,2,1,0,1,0,2,2,0,1,0,2,2,0,0,0,0,2,0,2,1,0,1,1,2,2,1,1,2,1,2,2,0,1,1,2,0,0,0,0,2,0,0,1,2,1,2,2,2,1,0,1,1,1,1,0,0,2,0,2,1,0,2,2,1,0,0,2,1,2,2,2,1,0,2,1,0,1,2,2,0,1,2,2,0,0,2,1,2,0,1,0,1,2,1,1,0,1,1,0,0,1,2,0,1,2,2,0,1,0,0,2,2,2,2,2,0,2,0,1,1,2,2,0,0,2,0,0,2,0,1,1,0,1,0,1,2,1,1,2,0,0,0,1,1,1,1,1,2,2,1,0,1,2,2,0,1,2,2,1,1,1,2,1,1,1,2,2,2,0,0,0,0,1,1,0,0,2,2,1,2,0,2,2,0,0,1,1,0,2,1,1,1,0,2,0,0,0,0,0,1,2,1,0,0,0,0,2,2,1,0,2,2,0,1,0,0,1,2,0,0,0,1,0,2,0,2,0,0,2,2,1,1,0,0,2,0,0,2,1,0,2,1,0,1,2,2,1,0,2,0,0,0,0,2,2,2,2,0,1,1,0,1,2,0,0,0,2,0,1,1,1,1,0,0,1,2,1,1,2,2,1,0,1,1,1,1,0,2,0,1,2,2,0,2,0,2,1,1,0,1,0,2,2,2,2,1,1,2,1,1,2,0,0,2,0,0,1,0,0,2,2,0,2,1,2,2,2,2,1,0,1,2,2,1,1,1,1,1,0,1,2,0,0,2,0,0,2,2,1,1,1,0,0,0,2,0,2,0,1,2,2,0,2,2,2,0,1,0,1,2,2,2,1,0,2,1,1,2,0,1,2,2,1,0,2,2,1,2,0,1,2,1,0,2,0,0,2,2,1,1,0,2,0,0,2,2,0,1,0,1,2,0,1,0,1,2,0,0,1,1,1,0,1,1,0,2,2,2,0,1,0,1,1,0,2,1,0,1,0,0,2,0,0,1,2,0,2,1,0,1,0,0,0,0,1,0,1,0,0,2,0,2,0,0,1,1,0,0,2,0,0,2,1,2,1,2,2,1,2,1,0,1,2,0,2,0,1,2,2,0,2,2,1,1,0,0,0,0,1,0,0,1,0,0,2,1,0,1,0,1,0,2,2,2,2,2,1,2,0,1,2,2,1,0,1,2,0,1,1,0,1,2,0,1,2,0,0,2,0,0,2,2,0,0,1,2,2,0,0,1,2,2,1,1,1,2,0,2,0,2,2,1,2,1,1,2,1,1,2,2,2,2,2,0,0,1,2,1,2,0,0,2,0,0,2,1,1,1,2,0,1,2,0,1,1,0,1,1,2,0,2,2,0,1,2,2,2,0,1,2,0,2,2,0,0,1,0,0,0,0,2,0,1,0,0,2,0,0,0,2,1,0,2,0,1,1,1,0,2,0,0,1,0,2,2,1,0,0,1,1,0,1,2,1,1,2,2,2,0,1,0,2,2,2,1,1,2,2,0,1,2,0,0,1,1,2,0,1,2,1,2,1,2,2,1,2,2,0,1,1,2,0,1,0,0,2,0,0,1,0,0,0,2,1,2,2,2,0,0,1,2,0,0,2,1,1,2,0,0,2,1,1,0,0,1,2,2,0,1,2,0,1,0,2,2,1,1,1,0,0,2,2,2,2,0,1,0,2,2,1,2,1,1,1,0,2,2,1,1,2,2,0,2,1,2,2,2,1,1,2,1,0,0,1,1,0,2,1,0,2,2,2,2,0,0,0,1,0,0,0,1,1,1,0,1,0,0,0,2,1,0,2,1,0,0,2,0,2,2,1,2,0,2,1,2,2,1,2,0,0,2,2,0,0,1,0,1,2,1,1,0,2,1,0,1,2,2,2,1,1,2,0,1,1,2,1,2,0,2,1,0,2,1,2,0,0,0,0,0,2,0,2,1,0,0,0,1,2,0,0,2,1,2,0,2,1,2,0,1,1,2,0,0,1,1,0,0,2,0,1,2,1,1,0,1,0,2,2,2,2,1,2,0,2,1,2,2,1,1,1,0,1,2,2,1,2,0,0,0,2,1,1,1,0,2,0,1,0,2,0,0,2,0,2,1,1,1,2,0,1,0,0,2,2,1,0,0,0,2,2,0,2,1,1,0,1,1,2,1,2,2,0,0,1,2,2,2,2,2,1,2,0,1,2,1,0,2,2,2,2,2,1,2,1,2,0,0,1,1,2,2,1,0,1,2,0,2,0,1,2,2,1,2,1,0,0,1,2,0,1,1,0,2,2,2,0,1,2,2,1,0,1,2,1,0,2,2,2,2,0,1,0,2,0,0,0,1,1,2,2,2,0,2,2,2,0,2,1,0,2,1,2,1,2,2,1,0,1,1,2,2,0,1,2,1,2,1,2,2,0,2,0,1,1,0,2,2,2,2,1,0,1,0,0,1,1,2,1,2,1,1,2,1,1,0,2,2,1,1,2,2,1,1,2,2,1,2,2,1,2,1,2,0,1,2,1,0,2,0,2,0,0,0,2,0,0,0,1,2,2,2,2,1,0,2,0,0,1,1,0,0,0,1,0,1,2,2,0,2,1,2,1,2,2,1,0,1,0,2,2,0,2,2,1,1,0,0,1,1,0,2,2,2,0,1,0,1,0,0,1,0,2,1,2,2,0,0,2,0,0,2,0,2,1,1,1,1,0,0,1,0,1,0,1,0,2,2,1,1,2,1,2,0,2,1,0,2,2,0,2,2,0,2,2,2,0,1,2,0,2,2,2,0,1,0,0,2,2,1,1,2,1,2,2,0,2,2,2,2,0,0,0,1,0,2,0,0,2,1,2,0,2,2,2,2,2,2,1,2,0,2,2,2,2,1,1,0,0,1,2,0,2,0,2,0,2,2,0,1,2,1,2,0,2,2,1,2,1,0,0,1,2,1,0,2,2,1,1,1,2,1,1,2,1,0,2,2,0,0,0,2,1,2,2,0,1,0,0,2,1,1,1,0,1,1,2,2,1,1,0,0,1,1,0,2,0,2,1,0,0,1,2,2,1,0,2,2,1,1,0,1,0,0,0,0,1,1,1,1,1,0,2,1,0,2,2,0,2,1,1,0,2,1,1,1,2,2,2,2,2,2,1,1,1,2,0,2,2,2,1,1,1,0,2,1,2,1,0,1,1,0,0,0,2,1,2,2,1,1,2,0,1,0,2,0,0,2,2,1,0,2,1,2,0,2,2,2,2,0,0,0,1,0,2,1,1,0,2,1,2,2,1,2,2,1,0,1,2,2,0,1,0,1,2,2,1,1,1,0,0,0,1,2,2,1,2,2,0,2,2,1,0,0,2,0,1,1,2,1,0,0,0,1,2,0,0,0,0,1,1,1,2,1,2,2,1,2,2,2,1,1,2,2,2,2,1,2,0,0,0,2,0,2,1,2,0,1,1,1,0,0,2,2,1,1,0,1,0,0,1,0,1,0,2,0,2,0,1,2,2,1,2,1,1,1,0,1,0,0,2,0,1,1,2,2,2,1,1,0,1,2,2,2,0,2,2,0,1,1,1,1,1,2,0,0,2,2,2,0,0,0,1,1,2,0,2,1,0,1,1,2,1,1,2,2,2,2,2,2,0,0,2,1,2,2,2,1,2,0,0,2,1,1,0,1,0,2,0,1,2,2,0,0,0,2,0,1,0,1,2,1,0,1,2,2,1,0,0,1,1,0,2,2,0,1,2,1,1,0,1,1,2,1,2,2,1,0,2,0,2,1,0,0,2,2,1,1,0,0,1,1,0,0,2,0,0,2,0,2,0,2,1,1,2,1,0,0,0,0,2,0,0,1,1,2,0,0,2,1,1,2,0,2,1,1,1,2,1,2,1,2,0,1,2,2,2,1,2,2,1,1,2,0,2,1,0,1,2,1,1,0,2,1,2,0,1,1,0,0,0,2,1,0,1,0,0,0,1,2,0,0,1,0,0,2,2,0,2,1,0,0,1,1,2,2,2,0,1,1,0,1,0,2,0,0,0,2,0,1,0,0,0,1,0,2,2,0,1,1,1,1,0,0,2,1,2,0,0,0,1,1,2,2,0,0,0,1,2,1,0,1,1,2,1,1,0,0,2,2,2,0,1,0,0,2,1,0,1,0,0,0,2,1,2,1,0,2,0,0,1,2,2,1,2,1,2,0,0,1,1,0,1,1,1,1,2,2,1,2,0,2,1,0,0,0,2,2,2,0,1,2,1,1,0,1,2,1,0,0,0,2,0,0,1,2,2,0,0,1,0,0,1,0,2,1,0,2,2,2,0,2,1,1,2,0,1,1,1,1,1,1,1,1,0,2,0,2,2,2,2,2,0,2,1,1,0,1,0,0,1,0,0,0,2,1,2,2,2,1,0,1,0,2,2,0,0,0,1,2,0,2,2,1,1,1,0,2,2,0,2,2,0,1,2,2,0,1,1,1,1,2,2,0,2,2,2,2,1,1,0,2,1,0,0,1,1,0,0,0,0,1,0,2,1,2,0,1,0,2,1,2,2,2,2,0,2,1,0,2,0,2,0,2,2,0,0,2,0,2,1,2,2,0,0,1,2,0,1,1,2,0,0,2,0,1,0,0,2,0,1,2,2,1,0,2,2,1,0,1,1,0,1,1,1,0,0,1,0,2,0,2,2,2,2,1,0,2,2,0,2,0,0,0,2,0,0,2,0,2,1,1,2,1,1,0,1,0,1,1,2,0,2,1,0,0,0,2,0,2,0,0,2,1,0,0,0,0,0,1,0,1,1,1,1,1,1,2,0,1,2,1,0,1,0,2,2,2,2,0,2,0,0,0,1,1,0,1,1,0,2,0,2,2,1,0,1,0,1,0,0,1,1,1,1,1,2,1,0,1,2,1,2,2,0,1,0,1,2,0,1,1,2,0,0,2,0,2,0,0,1,2,2,2,0,0,2,0,1,1,2,2,0,0,2,1,1,0,1,1,0,2,0,0,2,2,0,0,2,0,1,2,1,2,0,2,1,1,1,0,2,0,0,2,2,2,2,2,1,2,0,2,1,1,2,2,2,0,0,1,0,0,2,2,2,1,1,1,2,1,2,2,2,0,1,0,0,1,1,0,1,1,2,0,2,1,1,0,1,1,1,0,0,1,1,1,0,1,1,2,0,0,0,2,2,0,0,0,0,2,1,2,1,1,1,2,1,1,0,0,0,0,2,1,2,1,0,1,2,2,0,0,0,2,2,0,0,1,0,0,1,1,2,1,2,1,0,1,1,1,1,2,1,1,2,0,1,2,1,0,2,2,2,0,0,2,2,0,0,2,1,0,0,2,2,1,2,0,0,0,0,2,1,0,1,1,0,2,1,2,1,2,1,2,1,2,2,1,2,0,2,2,2,1,1,1,2,1,2,2,2,1,1,2,1,1,2,1,2,1,2,2,0,2,2,1,2,1,2,2,2,0,0,0,1,1,0,2,1,0,1,1,2,1,0,2,1,0,1,0,0,2,2,1,2,1,0,1,1,0,1,1,2,2,0,0,2,0,0,0,2,0,2,1,1,2,2,1,0,0,2,1,0,2,2,1,1,2,1,2,2,2,2,0,1,1,1,2,0,2,0,0,1,2,0,2,2,0,2,2,0,0,2,1,2,1,1,0,2,2,2,1,2,2,0,0,0,0,2,0,1,1,2,1,1,1,2,2,1,0,1,1,1,1,0,1,1,2,1,0,2,0,2,0,1,2,2,0,1,1,2,1,2,0,2,1,0,1,0,1,2,1,2,0,2,1,2,1,0,1,1,1,0,1,0,0,2,0,0,2,2,0,0,2,0,2,2,0,0,2,2,0,2,1,2,0,1,0,2,1,1,2,1,2,0,2,1,2,1,1,2,2,1,0,1,0,1,1,1,1,0,0,0,2,0,0,0,0,0,2,1,2,0,1,1,2,0,2,2,0,2,0,1,1,1,0,0,2,1,1,2,0,1,2,0,0,2,0,0,2,0,1,2,2,2,2,2,0,1,0,2,2,1,1,2,2,2,1,0,2,2,2,2,1,0,0,2,2,1,1,1,1,1,1,2,2,0,2,2,1,1,2,0,1,0,1,2,2,0,2,2,2,0,2,1,1,1,2,0,0,0,1,2,0,1,0,1,0,1,1,2,2,1,0,0,2,0,1,2,0,0,1,2,1,1,2,2,1,0,0,0,0,2,2,0,2,0,0,1,0,2,0,2,1,1,1,0,2,2,0,0,0,1,0,1,0,1,0,2,1,2,0,1,2,2,0,0,0,0,0,0,2,0,2,1,0,2,1,1,1,2,0,1,1,2,1,0,1,2,0,2,1,2,0,0,1,1,0,1,1,2,0,2,2,0,2,1,0,0,2,2,0,2,1,2,1,1,1,1,2,2,0,1,2,2,0,2,1,1,1,2,0,0,1,0,0,0,2,1,1,0,0,0,1,0,0,2,2,0,1,1,0,2,1,2,2,0,0,2,2,0,0,2,2,0,0,1,1,1,0,0,0,1,2,0,0,0,1,0,1,2,2,2,1,1,1,1,0,2,2,1,1,1,0,2,0,2,0,2,1,2,2,1,2,1,0,1,1,2,1,2,2,1,0,1,1,0,1,2,1,0,0,0,0,0,2,1,2,0,2,0,1,0,2,1,0,0,2,0,1,2,0,2,2,1,1,1,0,0,2,0,1,1,1,1,2,0,1,1,0,0,2,0,0,1,1,0,0,0,0,1,1,1,0,1,2,1,2,1,1,2,2,2,1,1,0,2,2,0,2,2,2,0,2,0,1,1,0,1,2,1,2,1,1,2,0,0,1,2,1,1,0,1,2,1,2,2,1,2,1,1,0,2,2,1,0,2,0,1,2,1,1,2,0,1,2,2,1,2,0,1,2,1,1,2,0,2,1,1,0,2,2,2,0,2,0,1,1,0,0,1,0,1,2,2,1,1,0,1,1,1,1,1,2,2,0,2,1,1,1,1,0,1,0,1,1,0,0,1,0,1,2,2,1,2,0,1,2,1,0,0,0,1,0,0,1,2,1,1,0,2,0,0,0,0,0,1,0,1,2,1,2,2,2,0,2,1,1,2,2,1,0,1,0,0,1,1,2,1,2,0,1,2,2,2,0,2,2,0,0,2,1,2,1,2,1,0,2,2,0,0,1,0,1,1,0,0,0,0,0,2,2,2,0,1,2,0,1,1,2,1,0,1,2,0,2,2,2,1,2,2,1,1,2,0,2,1,1,0,2,1,1,1,2,1,2,1,1,2,1,2,2,1,0,0,2,0,0,1,0,2,0,2,0,2,1,0,1,2,1,0,1,2,1,1,0,2,2,1,2,1,1,0,2,2,2,2,0,2,1,0,2,1,2,2,0,1,1,1,0,1,2,1,2,0,1,2,2,0,2,2,2,0,1,1,0,2,1,0,0,2,1,0,1,0,0,1,1,1,1,2,0,1,0,1,1,2,2,2,0,0,2,1,1,1,2,2,0,0,0,0,2,0,1,1,1,2,0,0,1,1,1,2,0,0,1,0,2,0,0,2,2,1,2,1,1,2,2,2,2,1,2,2,1,2,1,1,0,1,1,1,1,2,1,1,2,2,2,1,1,1,0,0,0,0,0,1,1,2,1,1,0,1,1,2,2,0,1,2,2,1,2,1,0,1,2,1,0,2,1,1,1,2,2,1,1,0,0,0,1,1,2,1,0,2,1,0,1,2,1,1,1,1,2,2,0,2,1,1,1,1,2,0,0,1,1,2,1,2,0,2,1,0,0,0,0,1,2,0,1,2,0,0,1,1,1,2,2,2,2,2,1,2,0,0,1,0,0,2,0,1,0,2,0,1,2,1,1,1,1,2,0,2,0,2,0,0,1,2,2,1,1,1,1,1,2,1,2,0,0,2,1,2,1,1,1,2,2,2,1,2,0,2,1,2,1,2,1,2,1,2,2,2,2,1,1,2,0,0,0,2,0,2,2,0,1,0,1,2,1,1,0,0,1,1,2,2,0,1,1,2,2,1,2,0,1,2,1,0,2,2,1,0,1,0,1,1,0,2,2,2,1,2,0,2,2,2,2,2,1,0,1,1,2,1,2,1,2,0,0,0,0,2,0,2,2,1,1,1,1,2,2,0,0,0,2,0,2,1,0,0,1,0,1,2,1,0,1,0,2,0,2,0,0,2,2,0,0,1,2,1,0,1,0,2,1,0,2,2,2,2,2,2,0,0,1,2,2,2,2,0,1,0,2,1,2,2,2,0,2,2,2,1,1,2,2,1,0,0,1,1,2,1,0,0,0,0,0,2,0,0,0,1,0,2,0,2,2,1,2,2,2,0,0,2,1,1,2,1,2,2,0,0,2,2,2,2,0,0,0,0,0,0,2,0,2,2,1,0,0,1,0,2,2,1,0,2,2,0,1,0,2,1,0,0,2,0,0,2,1,2,2,2,0,0,1,0,0,2,0,2,1,2,2,2,1,1,1,2,1,2,2,2,2,0,1,0,2,1,2,0,2,1,0,2,0,1,1,0,1,1,2,2,0,0,2,1,0,2,0,2,1,2,2,1,2,1,2,1,2,2,2,0,2,1,2,2,1,0,2,0,0,1,0,2,0,1,1,1,2,2,2,2,2,0,1,1,1,1,2,1,0,0,2,2,1,2,2,2,0,1,2,1,1,1,2,2,0,1,1,2,2,0,0,0,0,0,2,1,0,1,0,0,0,0,1,2,1,1,0,2,1,2,1,0,0,0,0,1,2,1,0,0,0,0,1,2,0,0,1,2,2,1,2,2,2,2,0,0,0,2,0,0,2,0,2,1,1,1,0,0,0,2,1,0,2,1,0,2,0,2,2,0,0,0,0,2,1,1,1,0,1,2,2,1,0,0,0,1,1,0,0,1,0,2,1,2,1,1,2,2,2,2,2,2,1,0,2,2,2,1,2,1,2,1,0,2,1,0,1,1,1,1,0,0,2,1,0,1,0,1,0,1,1,1,1,1,2,0,0,2,0,1,1,0,1,1,1,2,1,0,0,1,2,0,1,1,0,2,1,1,2,1,0,1,2,0,1,1,0,1,1,0,2,2,1,0,1,1,0,0,0,2,2,2,1,0,2,0,1,0,2,2,1,2,0,0,1,2,1,0,1,0,1,2,2,2,2,1,2,1,0,2,1,2,2,2,2,2,0,2,2,0,1,1,2,2,2,0,2,2,2,0,0,2,1,1,1,0,0,1,0,0,2,1,1,1,0,1,0,0,0,2,0,0,1,1,1,2,0,1,1,0,1,2,0,1,2,0,2,2,2,1,0,2,2,2,1,0,0,2,2,2,0,2,0,2,1,1,0,1,0,0,1,2,1,1,2,1,1,0,2,0,0,1,1,0,2,1,2,1,1,1,2,0,2,1,0,1,0,1,0,1,0,1,2,0,1,0,0,2,2,1,2,0,0,2,1,2,1,2,2,0,1,1,0,1,1,2,0,0,1,2,0,0,0,2,0,2,2,0,0,2,1,2,2,2,0,0,1,1,2,2,0,1,0,1,0,0,0,0,0,1,0,0,0,1,1,0,2,2,1,0,1,1,1,1,2,0,0,1,0,2,1,0,2,1,1,0,1,1,0,1,2,2,0,0,1,1,2,0,2,1,0,2,2,0,2,1,0,0,1,0,0,1,0,2,0,2,0,0,1,0,0,1,2,0,1,1,1,2,0,0,0,0,2,2,2,0,1,0,1,1,0,0,2,2,0,2,0,1,2,1,1,1,0,1,0,2,0,1,2,0,2,2,0,1,1,1,2,1,1,0,1,2,2,0,1,0,1,0,1,2,1,1,0,0,2,1,2,2,2,0,1,2,0,2,1,1,0,2,1,2,1,2,0,2,0,0,1,0,1,0,1,1,0,1,0,0,1,2,2,2,2,2,2,2,1,2,2,1,2,0,1,0,0,0,1,0,2,2,1,0,1,1,0,2,2,1,0,2,2,1,1,0,0,0,1,2,2,1,2,0,2,0,1,0,2,2,0,0,2,0,1,2,2,1,1,2,2,1,1,1,2,0,0,0,0,2,0,0,1,1,2,1,1,1,1,0,0,1,1,1,0,2,0,0,1,1,2,2,2,0,0,1,0,0,2,1,2,1,2,0,1,2,2,0,2,1,1,0,0,0,2,0,2,0,1,2,0,1,2,1,0,1,1,0,0,0,1,2,1,0,2,0,2,0,0,1,1,0,0,0,1,1,0,1,2,1,0,2,1,1,0,1,1,2,1,1,1,0,2,2,2,1,0,1,0,1,2,1,2,1,2,0,0,2,2,1,0,2,2,2,2,2,0,1,0,1,1,2,1,1,2,1,1,1,2,1,1,2,1,0,0,2,2,0,0,1,1,2,1,1,0,0,0,2,0,2,2,1,0,2,0,0,1,2,1,2,2,1,2,0,0,2,0,0,0,2,2,1,0,1,2,2,1,1,1,1,1,1,1,1,2,1,0,2,0,0,0,0,1,0,0,1,2,1,2,2,2,0,2,2,0,1,2,0,1,0,2,0,2,1,1,1,0,2,1,2,1,2,0,1,0,2,2,2,0,1,1,1,2,2,2,0,1,0,2,2,2,2,0,0,0,2,1,2,2,1,2,0,1,1,1,0,0,1,1,1,2,1,1,2,2,2,0,0,0,2,2,1,1,0,2,1,2,1,1,2,1,1,2,0,1,1,1,1,2,2,2,2,2,1,1,0,0,2,1,2,0,2,2,1,1,1,2,2,0,1,2,0,0,0,0,0,2,0,2,2,1,2,0,2,1,0,1,2,2,2,0,2,2,2,2,1,2,1,2,2,0,0,2,2,0,1,2,0,2,1,0,2,1,1,2,1,2,2,1,2,2,2,0,1,1,0,0,1,0,2,2,0,1,2,1,0,2,2,0,1,0,2,2,1,1,0,2,1,1,2,2,1,2,2,1,0,1,2,0,1,1,1,0,2,0,0,2,2,0,2,1,0,2,0,1,0,0,1,0,1,0,2,2,1,1,0,1,0,1,0,1,2,2,2,2,1,2,1,0,0,2,1,0,0,0,1,2,2,0,1,1,2,2,0,1,0,0,1,0,1,1,1,2,0,2,0,0,1,1,1,0,1,1,2,2,2,1,0,0,2,2,0,2,2,1,2,0,0,2,2,0,0,2,2,0,0,1,0,2,1,0,1,1,0,2,0,0,0,0,2,1,1,2,0,0,2,1,0,0,1,2,1,1,0,0,0,2,2,2,1,2,1,0,1,1,1,0,1,0,0,2,0,0,1,0,2,2,2,2,2,1,1,0,0,0,1,1,0,2,1,1,1,2,1,0,0,1,0,2,2,2,0,1,1,0,1,1,2,0,1,2,1,0,2,1,0,0,2,1,0,2,1,2,2,1,2,0,2,2,0,0,1,0,2,2,1,2,1,2,2,1,1,0,0,2,2,1,1,2,2,1,2,0,0,0,2,2,2,0,1,0,2,1,2,2,2,2,2,1,0,1,0,1,0,0,0,1,1,0,2,1,2,0,1,0,1,1,0,0,1,1,0,2,0,0,1,1,2,0,2,1,0,0,2,0,1,2,0,0,0,1,1,0,2,0,2,0,2,0,0,1,1,0,0,0,2,0,2,1,0,1,0,1,0,1,2,1,1,0,0,1,2,1,0,2,0,1,1,1,2,2,2,2,0,1,0,0,1,2,2,2,2,1,0,0,0,2,2,1,1,1,2,0,1,0,0,1,1,1,1,1,2,0,2,1,1,2,2,1,1,2,2,2,0,2,2,2,1,1,2,1,1,0,1,2,0,1,2,0,2,0,2,2,0,2,1,0,2,0,1,1,0,2,1,1,2,0,1,1,1,2,1,2,1,2,2,1,1,0,0,2,2,1,2,0,1,1,2,1,1,1,1,0,1,0,2,0,1,1,1,0,0,0,1,1,1,1,0,0,2,1,2,2,1,1,2,1,0,1,2,1,1,1,1,0,0,1,0,0,0,0,0,1,0,1,1,0,2,0,2,1,1,0,2,2,2,0,2,1,2,2,1,1,1,1,1,0,0,0,1,2,2,2,0,0,0,0,2,1,0,1,0,2,1,0,1,0,1,2,0,1,0,2,1,1,1,0,2,1,2,0,1,1,1,0,0,0,0,2,0,0,2,0,2,1,0,1,0,0,0,1,1,0,2,1,2,1,2,2,0,1,2,0,2,1,1,0,1,1,1,2,0,0,1,2,1,2,0,1,2,1,2,0,1,2,1,0,1,2,1,0,1,1,1,0,1,1,2,0,1,0,0,1,1,1,1,1,0,2,2,0,2,2,0,1,1,2,1,2,0,2,1,0,2,1,1,1,2,0,0,2,1,2,2,2,2,2,1,0,2,2,0,1,1,0,2,2,1,1,0,2,1,2,0,0,2,1,1,2,0,0,0,0,2,2,0,1,1,0,2,2,1,2,1,1,0,2,2,0,1,2,1,2,1,0,1,1,0,0,2,2,2,0,0,2,2,0,0,0,0,0,0,1,1,0,2,0,0,2,0,2,0,0,0,2,1,2,2,1,0,2,2,1,2,2,0,2,0,1,0,0,1,2,1,0,1,0,0,1,0,0,0,1,1,1,2,2,2,1,0,2,2,2,0,2,1,2,1,2,0,1,1,0,0,0,2,2,1,1,1,2,0,2,1,1,1,0,0,1,2,2,0,0,0,1,1,2,1,2,0,2,1,2,2]
,25000000))