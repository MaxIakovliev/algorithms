class Solution:


    def smallestDistancePair0(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Simple solution, but not effective  in terms of time cost O(n^2)
        """
        dists=[]
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                dists.append(abs(nums[j]-nums[i]))
        dists.sort()
        return dists[k-1]

    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def countPairs2(nums:list,mid:int)->(int):
            n=len(nums)
            res=0
            for i in range(n):
                res +=upperBound(nums, i, n-1, nums[i]+mid)-i-1
            return  res
        
        def upperBound(nums:[int], lo:int, hi:int, key:int)->(int):
            if (nums[hi]<=key):
                return hi+1
            while(lo<hi):
                mid=(int)((lo+hi)/2)
                if (key>=nums[mid]):
                    lo=mid+1
                else:
                    hi=mid
            return lo


        nums.sort()
        n=len(nums)
        lo=nums[1]-nums[0]
        for i in range(1,n-1):
            lo=min(lo, nums[i+1]-nums[i])

        hi=nums[n-1]-nums[0]
        while lo<hi:
            mid=(int)((lo+hi)/2)
            if countPairs2(nums,mid)<k:
                lo=mid+1
            else:
                hi=mid
        return lo


if __name__ =="__main__":
    c=Solution()
    print(c.smallestDistancePair([1,3,1],1)) #0
    print(c.smallestDistancePair([62,100,4],2)) #58
    print(c.smallestDistancePair([1,2,0,2,1,0,1,1,0,2,2,0,2,0,1,1,1,0,1,0,1,1,2,2,2,2,0,0,2,1,2,1,2,0,0,0,1,0,0,1,0,2,1,1,1,1,0,2,2,1,0,2,0,2,2,2,1,0,2,2,2,2,0,0,1,0,1,1,2,1,2,2,1,1,0,2,0,1,0,1,1,2,0,1,1,1,1,2,0,2,2,0,0,1,1,1,1,2,1,2,2,1,2,0,1,2,2,1,1,2,1,0,1,1,1,0,0,1,2,0,2,1,0,1,2,0,2,2,1,0,0,2,0,1,1,0,1,0,1,0,1,2,2,2,0,1,1,1,1,1,0,2,2,2,1,0,1,0,1,0,0,0,0,2,0,0,1,1,2,0,2,1,2,0,0,1,0,1,2,1,0,1,1,1,1,0,0,2,2,1,1,0,0,0,0,1,2,2,1,1,0,1,2,0,0,2,1,2,1,2,0,2,1,1,2,2,2,2,2,0,1,1,0,1,2,2,0,2,2,2,0,2,0,1,1,2,2,0,2,2,2,2,2,2,1,0,2,2,2,0,2,0,2,0,2,1,0,1,0,1,1,0,2,0,1,0,0,2,0,0,0,2,0,2,2,0,2,0,0,1,1,0,2,0,1,2,2,0,1,1,2,0,0,0,2,1,0,1,0,2,1,2,0,1,2,1,1,1,0,1,2,1,2,2,1,2,0,2,1,0,1,1,1,2,0,2,2,2,2,1,0,2,2,1,1,1,1,0,1,2,2,0,1,2,2,1,0,0,1,2,1,0,2,1,1,1,0,0,0,1,1,1,0,2,0,2,0,1,2,2,0,2,1,2,2,0,0,0,0,2,1,1,2,0,2,0,1,0,1,0,2,0,0,0,2,1,2,0,1,2,1,2,1,0,1,0,1,0,0,1,2,1,1,2,1,1,2,2,1,0,1,1,2,2,1,2,2,2,1,0,1,1,1,0,0,0,2,1,1,1,2,2,1,2,0,2,1,2,0,2,2,2,1,1,2,2,0,0,2,2,2,1,2,2,1,0,2,0,2,0,2,1,2,2,1,1,1,1,1,0,0,1,0,2,2,0,0,2,1,0,1,0,2,1,0,0,0,0,1,2,1,2,0,0,1,1,2,2,2,2,0,2,1,0,0,0,2,0,1,1,0,2,1,1,1,2,1,0,0,1,0,1,0,1,2,0,2,1,0,0,1,2,1,1,0,0,0,2,2,2,1,1,2,2,0,1,0,2,2,2,0,1,0,0,1,0,0,1,1,1,1,1,1,2,1,2,0,2,0,2,1,2,2,2,0,1,0,1,2,0,2,2,1,2,0,1,2,2,0,1,1,0,1,1,0,0,0,1,2,1,0,0,2,0,1,0,2,2,0,1,0,0,0,1,0,0,0,2,1,1,1,1,1,0,1,1,0,1,0,1,0,2,2,0,2,2,0,0,1,2,0,1,1,1,2,0,0,0,2,0,2,2,2,2,1,0,2,2,0,0,1,1,2,2,2,1,1,2,0,1,0,0,1,0,1,2,0,1,2,0,1,1,1,1,2,0,1,0,1,2,2,0,0,2,0,1,2,1,2,1,0,0,1,0,0,1,2,0,1,0,0,0,0,2,0,1,0,1,2,0,1,2,0,0,0,0,1,1,2,0,0,0,2,1,1,0,0,2,2,1,0,0,1,0,1,0,1,1,0,2,0,1,1,2,2,1,1,0,2,0,0,1,0,1,2,2,1,2,2,2,2,2,1,2,0,0,0,1,1,0,0,2,1,0,1,0,2,2,0,1,2,2,2,0,0,0,2,2,1,2,1,0,0,0,1,1,2,1,2,0,1,2,1,0,1,2,0,1,2,1,2,1,1,1,2,2,1,0,1,0,2,1,2,0,2,0,0,0,1,2,1,0,0,0,1,2,0,2,2,2,1,0,2,2,1,1,2,0,0,1,2,2,2,1,2,1,2,1,0,2,2,0,0,0,2,0,1,0,1,0,2,2,2,2,0,1,1,1,1,0,1,0,0,1,2,0,1,0,0,2,0,1,1,1,1,2,0,1,1,2,0,2,1,2,1,1,0,1,1,2,1,2,0,1,0,0,0,1,0,2,0,0,2,0,0,1,0,1,2,2,1,2,0,2,2,2,0,2,0,2,1,0,0,0,0,0,0,1,0,2,0,1,1,0,2,1,2,1,1,0,2,1,2,0,1,1,1,0,1,0,1,0,0,1,1,0,1,1,0,2,2,1,1,0,1,0,0,0,2,2,2,0,1,2,1,2,0,2,1,0,0,1,2,2,1,0,1,2,0,0,2,1,1,2,0,0,1,0,2,2,2,2,0,1,0,0,0,1,1,0,2,0,2,0,2,2,2,0,2,0,0,2,1,0,2,2,2,1,2,0,2,2,0,2,1,2,2,0,1,0,2,0,1,1,2,2,2,2,0,0,0,0,2,2,2,2,1,0,2,0,2,0,1,0,1,1,2,2,1,2,1,2,0,1,2,2,2,0,1,0,1,0,1,0,1,0,1,2,2,0,2,2,2,0,1,0,2,1,1,1,0,0,0,0,0,2,0,1,0,2,0,0,2,2,2,2,1,2,2,1,2,0,1,0,1,1,0,0,2,2,1,2,2,1,0,0,0,0,0,0,1,1,0,1,0,2,0,1,0,2,2,2,0,1,0,2,1,2,2,0,2,1,1,1,1,1,1,2,2,1,0,1,2,1,1,0,0,1,0,2,0,2,2,2,2,1,2,2,2,2,1,2,2,1,1,1,0,1,2,2,0,0,2,1,0,2,1,0,2,2,0,2,1,0,2,1,0,0,0,0,2,0,1,0,2,0,1,2,2,0,1,0,1,1,1,2,1,0,0,0,0,0,2,0,1,1,1,0,1,2,2,1,2,2,0,2,2,0,0,0,2,2,2,1,1,2,1,2,1,2,1,1,0,0,2,0,2,0,1,1,0,0,2,1,0,0,1,2,0,1,0,2,1,1,1,1,2,2,0,2,2,0,1,1,2,2,0,2,0,1,0,2,0,2,2,2,1,2,2,0,1,1,2,2,1,2,2,2,2,2,2,0,0,1,1,0,0,1,0,0,0,2,1,2,1,2,2,1,1,0,2,1,0,0,1,2,2,1,1,1,1,0,0,0,2,0,0,2,1,1,2,2,2,1,2,1,0,1,2,1,2,2,1,1,0,0,0,1,1,1,0,0,1,1,1,2,2,1,2,1,0,2,0,1,0,0,2,0,0,0,2,1,0,2,0,2,1,1,2,0,1,1,0,2,0,1,2,2,0,0,2,0,1,1,0,2,2,1,0,0,0,2,0,1,0,0,0,2,0,2,2,1,0,1,2,2,2,2,1,1,2,2,2,0,1,2,0,2,1,2,1,0,2,0,1,0,0,2,1,0,0,0,2,0,0,1,2,2,0,0,1,0,1,1,2,2,2,0,2,1,0,2,0,1,2,1,0,1,1,1,2,1,0,0,0,2,1,0,2,2,0,1,0,2,0,2,2,2,0,1,2,2,2,1,0,0,1,0,0,0,1,1,0,1,2,2,2,0,1,0,0,1,2,2,2,0,1,1,1,2,0,2,1,1,2,2,1,0,1,2,0,2,1,1,0,1,1,2,0,1,0,2,1,2,0,2,2,2,2,0,2,0,2,1,0,1,0,2,1,0,0,0,2,0,0,0,1,0,2,1,0,0,0,0,0,2,1,0,0,0,2,1,2,0,0,0,2,2,2,2,1,1,1,0,1,2,2,0,0,1,1,0,2,0,2,1,2,0,0,2,1,0,0,0,2,2,0,1,1,0,0,0,0,1,0,1,1,2,1,2,1,2,0,1,1,2,0,0,2,1,0,0,2,0,1,2,1,1,2,2,2,1,2,2,0,1,2,0,1,2,1,2,0,2,1,0,2,1,1,2,0,2,0,1,2,2,1,2,1,1,1,1,2,1,2,1,2,0,1,1,1,2,0,1,2,1,1,0,2,1,0,2,0,0,0,2,1,0,1,2,0,1,0,1,1,0,0,1,0,2,0,0,0,0,2,2,0,1,1,2,1,2,2,1,0,1,1,2,2,0,1,0,1,0,2,1,0,2,0,2,2,1,1,1,1,2,2,2,2,0,1,1,0,2,0,1,2,1,2,0,0,2,2,1,2,2,1,1,0,0,0,0,2,1,0,2,2,0,1,2,2,2,1,1,2,2,2,2,2,2,2,2,2,0,0,1,2,2,0,2,0,1,2,2,1,0,2,2,0,0,0,2,0,0,0,1,2,1,0,2,2,1,2,0,0,2,2,2,1,1,1,2,0,0,2,0,0,2,1,2,2,2,1,0,0,1,1,1,0,0,2,0,1,1,0,0,0,1,0,2,0,0,1,1,2,0,2,0,2,0,1,0,0,1,1,0,1,0,1,1,0,2,1,0,1,0,1,2,0,0,1,2,0,2,1,0,1,1,2,0,2,2,1,1,2,2,1,1,0,2,2,2,2,1,2,0,2,0,2,2,1,1,0,1,0,0,1,2,2,1,1,1,0,1,0,1,2,0,2,1,2,2,0,2,2,0,1,1,0,0,1,1,1,1,1,0,1,2,0,2,2,0,1,2,2,1,1,2,0,1,1,1,2,0,2,1,1,2,1,1,1,1,2,1,0,1,2,0,1,1,1,0,2,1,2,0,0,2,1,0,1,0,2,2,2,1,1,1,2,2,0,2,1,0,2,2,2,2,2,2,0,0,1,2,2,2,0,0,2,0,2,2,2,2,2,2,2,0,2,1,1,2,0,2,2,0,2,1,0,0,1,1,1,1,2,1,2,0,2,0,0,0,2,2,0,0,2,1,2,1,0,1,0,2,0,1,2,0,1,2,0,1,1,1,1,0,2,2,1,0,2,1,0,2,0,1,0,0,2,1,0,1,0,2,2,2,1,2,2,0,2,1,0,2,0,2,1,1,2,0,1,2,0,0,1,1,1,0,2,0,0,2,2,0,0,2,2,1,0,1,2,1,1,2,1,0,0,1,0,0,0,0,0,1,2,2,2,1,1,2,0,1,2,1,2,1,1,1,1,1,0,2,1,1,1,0,2,0,0,0,2,1,0,1,2,0,1,1,2,1,1,2,2,0,2,0,2,0,2,0,2,2,0,0,1,0,2,0,0,0,0,0,1,0,2,1,1,0,1,2,2,1,0,2,2,1,2,0,1,2,2,2,0,1,0,0,1,0,2,1,0,1,1,1,1,2,1,2,0,1,2,2,2,2,2,0,1,0,2,2,0,0,0,0,1,2,1,1,1,1,0,1,0,0,0,0,2,2,2,0,0,0,1,2,2,2,2,2,2,2,1,2,1,1,1,2,0,1,1,2,0,0,1,2,0,2,0,2,2,1,2,2,2,2,2,1,1,2,1,1,1,2,0,1,2,2,1,1,0,2,1,2,1,1,1,0,2,1,0,0,2,2,2,1,0,1,2,1,2,1,1,0,0,0,2,1,0,1,0,0,1,2,0,0,2,0,0,0,1,0,1,0,1,0,1,0,1,1,1,0,2,2,0,0,0,1,2,0,1,1,1,1,2,1,1,0,1,1,1,0,1,1,2,1,2,2,1,2,2,2,1,1,0,2,1,0,2,0,1,1,0,1,2,1,1,0,2,0,0,1,0,0,1,0,0,1,2,2,0,1,2,1,2,2,2,2,0,2,1,1,0,0,0,1,1,2,2,0,0,0,1,2,0,1,2,0,1,2,1,1,2,1,2,2,0,1,2,2,1,2,0,1,1,0,0,0,0,1,2,2,2,0,1,0,1,0,2,1,1,0,2,1,2,1,2,0,2,0,0,1,2,0,1,0,0,0,1,1,1,2,1,1,1,0,1,2,0,0,0,1,0,2,0,2,0,1,1,1,0,0,0,2,0,1,2,0,1,0,1,1,0,1,0,1,1,2,1,1,2,2,1,1,1,0,1,0,1,1,2,1,2,2,1,1,2,2,2,1,1,1,1,1,1,2,1,1,0,2,1,0,0,1,1,1,0,2,2,0,0,1,1,2,2,1,2,2,2,0,0,2,2,2,0,1,0,2,1,0,0,2,0,0,1,2,1,2,1,2,0,0,1,0,2,0,0,2,0,1,1,2,2,0,1,0,1,1,1,2,2,1,1,1,2,0,1,2,0,1,1,1,0,1,0,2,2,0,2,1,0,0,1,2,0,0,1,0,1,0,2,2,1,0,1,2,2,0,2,2,0,0,1,1,1,2,1,2,2,2,0,1,0,0,0,1,0,0,0,1,1,0,2,1,0,2,1,2,0,2,0,2,2,0,2,2,0,1,0,0,2,0,2,2,1,0,2,0,2,2,1,1,2,2,2,1,0,0,1,2,1,0,1,0,2,2,1,2,1,2,0,1,0,1,2,2,1,0,2,0,2,1,0,1,2,0,0,2,2,1,1,0,0,1,2,0,2,2,1,2,1,0,1,1,0,0,2,2,2,2,2,0,1,0,1,1,1,0,1,2,1,0,2,2,0,1,1,2,0,2,2,0,2,1,1,2,2,2,1,1,0,1,0,2,2,2,2,0,2,2,1,0,0,1,1,0,1,2,1,0,0,0,2,2,0,2,0,1,2,2,1,1,1,2,0,2,0,0,1,2,0,1,1,0,1,1,1,2,0,0,0,2,1,0,2,1,2,1,0,1,1,2,2,0,1,0,2,2,2,1,1,0,1,2,1,2,0,0,0,0,1,1,1,1,0,2,1,0,0,2,0,2,0,1,1,0,0,1,2,0,2,2,2,1,1,0,0,0,0,1,0,1,2,2,2,0,1,0,1,1,0,0,1,0,0,1,1,2,2,0,0,2,2,0,0,0,2,2,2,2,1,1,2,2,2,0,0,2,0,1,2,2,2,2,0,0,2,0,2,2,2,0,2,1,1,1,1,0,2,0,2,0,0,1,2,2,1,0,2,0,1,2,2,1,2,0,0,2,0,0,1,1,1,0,2,0,2,2,2,2,1,2,2,0,1,2,2,2,0,0,0,1,0,1,2,0,0,0,0,1,2,0,0,2,2,0,1,1,2,2,2,2,0,0,0,1,0,1,0,1,1,0,0,0,2,2,0,0,1,1,0,2,2,1,1,0,2,0,2,1,0,1,2,1,1,2,1,0,0,1,2,1,1,2,2,0,1,2,0,0,0,1,1,2,0,2,1,2,0,1,0,0,0,2,0,1,1,2,2,2,0,0,0,2,2,1,0,2,1,0,0,2,1,1,2,0,2,0,2,0,1,2,2,0,0,0,2,2,1,1,1,0,0,1,1,0,0,0,2,1,1,0,1,0,2,0,1,0,2,0,2,1,0,1,2,0,0,2,1,1,0,0,1,0,2,1,1,1,2,1,2,2,0,2,2,1,2,2,2,1,0,1,1,1,2,1,1,1,1,0,0,1,1,0,2,2,0,1,1,1,1,2,1,1,0,0,2,2,0,2,1,1,1,1,2,0,2,2,2,0,1,0,1,0,0,1,0,2,0,0,0,2,1,1,2,2,0,1,1,0,0,1,0,2,0,2,2,0,2,2,0,0,1,2,0,1,0,0,0,0,1,2,0,1,1,0,0,2,0,0,2,0,1,1,2,2,1,0,1,0,0,2,2,2,0,0,1,0,2,0,1,2,1,0,1,1,2,2,2,2,0,0,0,2,1,1,2,0,1,1,1,0,0,0,1,0,2,0,2,0,2,0,0,1,0,0,2,0,2,2,2,2,2,1,0,2,0,0,0,0,0,0,2,0,2,0,1,0,2,2,2,1,1,1,0,1,0,1,1,0,2,0,0,1,2,2,1,2,0,0,0,2,2,0,1,1,0,2,0,1,2,1,0,0,0,1,1,1,2,0,1,1,1,2,1,0,2,1,0,1,0,1,2,0,1,2,0,2,0,0,0,2,0,2,2,2,0,1,1,2,0,0,1,1,0,1,1,0,2,0,1,1,2,2,1,0,2,1,2,0,0,0,2,2,2,0,1,1,0,0,1,1,1,1,0,0,2,0,2,2,0,1,0,0,1,1,1,1,1,0,0,2,0,0,2,0,2,2,2,2,1,1,1,2,0,2,1,1,0,0,1,2,1,2,2,2,2,0,0,0,1,1,0,1,0,1,1,1,2,0,2,2,2,0,1,0,1,2,2,0,0,2,0,0,1,0,0,1,2,1,0,1,2,2,1,2,2,1,1,0,2,1,0,1,1,2,1,2,1,0,2,0,1,1,0,0,1,0,2,1,1,1,2,1,0,2,2,1,2,2,1,2,2,2,2,1,1,2,1,0,0,2,2,1,1,2,1,1,1,0,0,0,0,0,0,2,2,1,0,1,0,1,1,2,2,0,1,1,2,2,1,0,2,1,1,1,2,1,2,0,0,2,0,2,0,0,0,0,2,2,2,0,0,0,2,0,2,1,0,2,1,1,0,1,0,0,2,2,1,1,2,0,0,0,1,1,1,1,1,0,2,2,2,2,1,0,0,0,1,0,1,1,0,1,2,2,1,0,1,1,0,2,0,2,2,1,1,1,1,0,0,2,2,1,2,0,0,2,1,0,2,1,2,1,2,1,0,2,2,2,0,0,1,1,0,0,1,1,1,1,2,2,2,1,0,2,0,2,2,2,1,1,1,0,0,1,1,0,1,0,0,2,1,2,0,0,0,1,2,0,1,2,0,1,0,0,0,1,0,1,2,2,1,2,0,1,0,2,1,0,1,2,1,1,1,2,1,0,0,2,1,1,1,0,2,1,2,2,2,2,2,1,1,2,1,2,1,0,1,1,0,1,2,0,1,2,2,2,2,2,1,0,2,2,2,2,0,1,2,1,2,0,0,2,0,0,0,0,0,0,2,0,0,2,0,2,1,1,2,0,1,1,2,0,0,2,2,0,0,2,0,2,2,1,0,1,0,2,0,0,0,0,2,0,1,2,1,0,1,2,0,2,0,2,1,0,0,0,1,2,0,1,1,2,1,1,1,0,0,0,0,0,2,2,0,2,2,2,1,2,1,1,1,2,0,2,1,0,0,0,2,2,1,0,2,0,2,0,1,0,1,0,2,0,1,1,1,1,0,2,0,1,2,1,2,0,2,1,2,1,2,2,2,2,1,2,0,0,2,0,2,2,2,0,1,2,1,0,2,0,2,2,2,0,1,1,0,2,2,2,2,0,1,2,1,2,2,1,2,0,1,2,0,0,0,2,2,1,1,0,0,2,1,1,1,0,1,2,0,1,2,0,0,1,2,0,2,0,0,2,0,2,0,1,1,1,1,1,0,2,1,1,2,2,0,0,1,2,1,2,2,1,0,2,2,2,2,2,0,1,0,0,1,1,2,0,1,2,1,2,0,0,0,2,2,2,1,2,1,1,2,0,0,0,0,1,1,1,0,1,0,2,0,1,1,2,2,0,0,1,2,0,2,2,1,2,0,0,1,0,1,2,2,0,1,2,1,2,1,2,1,2,0,1,1,1,1,1,2,0,2,2,1,2,2,1,1,0,0,1,0,2,0,1,1,1,1,2,2,0,0,1,0,1,0,2,2,2,1,0,2,2,2,0,0,2,2,1,2,2,0,2,0,2,1,0,2,0,0,1,1,1,0,2,0,0,0,1,0,2,1,2,1,2,1,0,1,2,0,2,0,1,2,2,1,0,1,2,1,2,1,0,2,2,2,1,1,1,0,0,1,1,1,1,1,1,2,1,1,1,0,0,2,0,1,2,2,0,1,2,2,2,2,0,2,1,1,2,2,2,2,1,0,1,0,2,2,0,1,0,2,2,0,0,0,0,2,0,2,1,0,1,1,2,2,1,1,2,1,2,2,0,1,1,2,0,0,0,0,2,0,0,1,2,1,2,2,2,1,0,1,1,1,1,0,0,2,0,2,1,0,2,2,1,0,0,2,1,2,2,2,1,0,2,1,0,1,2,2,0,1,2,2,0,0,2,1,2,0,1,0,1,2,1,1,0,1,1,0,0,1,2,0,1,2,2,0,1,0,0,2,2,2,2,2,0,2,0,1,1,2,2,0,0,2,0,0,2,0,1,1,0,1,0,1,2,1,1,2,0,0,0,1,1,1,1,1,2,2,1,0,1,2,2,0,1,2,2,1,1,1,2,1,1,1,2,2,2,0,0,0,0,1,1,0,0,2,2,1,2,0,2,2,0,0,1,1,0,2,1,1,1,0,2,0,0,0,0,0,1,2,1,0,0,0,0,2,2,1,0,2,2,0,1,0,0,1,2,0,0,0,1,0,2,0,2,0,0,2,2,1,1,0,0,2,0,0,2,1,0,2,1,0,1,2,2,1,0,2,0,0,0,0,2,2,2,2,0,1,1,0,1,2,0,0,0,2,0,1,1,1,1,0,0,1,2,1,1,2,2,1,0,1,1,1,1,0,2,0,1,2,2,0,2,0,2,1,1,0,1,0,2,2,2,2,1,1,2,1,1,2,0,0,2,0,0,1,0,0,2,2,0,2,1,2,2,2,2,1,0,1,2,2,1,1,1,1,1,0,1,2,0,0,2,0,0,2,2,1,1,1,0,0,0,2,0,2,0,1,2,2,0,2,2,2,0,1,0,1,2,2,2,1,0,2,1,1,2,0,1,2,2,1,0,2,2,1,2,0,1,2,1,0,2,0,0,2,2,1,1,0,2,0,0,2,2,0,1,0,1,2,0,1,0,1,2,0,0,1,1,1,0,1,1,0,2,2,2,0,1,0,1,1,0,2,1,0,1,0,0,2,0,0,1,2,0,2,1,0,1,0,0,0,0,1,0,1,0,0,2,0,2,0,0,1,1,0,0,2,0,0,2,1,2,1,2,2,1,2,1,0,1,2,0,2,0,1,2,2,0,2,2,1,1,0,0,0,0,1,0,0,1,0,0,2,1,0,1,0,1,0,2,2,2,2,2,1,2,0,1,2,2,1,0,1,2,0,1,1,0,1,2,0,1,2,0,0,2,0,0,2,2,0,0,1,2,2,0,0,1,2,2,1,1,1,2,0,2,0,2,2,1,2,1,1,2,1,1,2,2,2,2,2,0,0,1,2,1,2,0,0,2,0,0,2,1,1,1,2,0,1,2,0,1,1,0,1,1,2,0,2,2,0,1,2,2,2,0,1,2,0,2,2,0,0,1,0,0,0,0,2,0,1,0,0,2,0,0,0,2,1,0,2,0,1,1,1,0,2,0,0,1,0,2,2,1,0,0,1,1,0,1,2,1,1,2,2,2,0,1,0,2,2,2,1,1,2,2,0,1,2,0,0,1,1,2,0,1,2,1,2,1,2,2,1,2,2,0,1,1,2,0,1,0,0,2,0,0,1,0,0,0,2,1,2,2,2,0,0,1,2,0,0,2,1,1,2,0,0,2,1,1,0,0,1,2,2,0,1,2,0,1,0,2,2,1,1,1,0,0,2,2,2,2,0,1,0,2,2,1,2,1,1,1,0,2,2,1,1,2,2,0,2,1,2,2,2,1,1,2,1,0,0,1,1,0,2,1,0,2,2,2,2,0,0,0,1,0,0,0,1,1,1,0,1,0,0,0,2,1,0,2,1,0,0,2,0,2,2,1,2,0,2,1,2,2,1,2,0,0,2,2,0,0,1,0,1,2,1,1,0,2,1,0,1,2,2,2,1,1,2,0,1,1,2,1,2,0,2,1,0,2,1,2,0,0,0,0,0,2,0,2,1,0,0,0,1,2,0,0,2,1,2,0,2,1,2,0,1,1,2,0,0,1,1,0,0,2,0,1,2,1,1,0,1,0,2,2,2,2,1,2,0,2,1,2,2,1,1,1,0,1,2,2,1,2,0,0,0,2,1,1,1,0,2,0,1,0,2,0,0,2,0,2,1,1,1,2,0,1,0,0,2,2,1,0,0,0,2,2,0,2,1,1,0,1,1,2,1,2,2,0,0,1,2,2,2,2,2,1,2,0,1,2,1,0,2,2,2,2,2,1,2,1,2,0,0,1,1,2,2,1,0,1,2,0,2,0,1,2,2,1,2,1,0,0,1,2,0,1,1,0,2,2,2,0,1,2,2,1,0,1,2,1,0,2,2,2,2,0,1,0,2,0,0,0,1,1,2,2,2,0,2,2,2,0,2,1,0,2,1,2,1,2,2,1,0,1,1,2,2,0,1,2,1,2,1,2,2,0,2,0,1,1,0,2,2,2,2,1,0,1,0,0,1,1,2,1,2,1,1,2,1,1,0,2,2,1,1,2,2,1,1,2,2,1,2,2,1,2,1,2,0,1,2,1,0,2,0,2,0,0,0,2,0,0,0,1,2,2,2,2,1,0,2,0,0,1,1,0,0,0,1,0,1,2,2,0,2,1,2,1,2,2,1,0,1,0,2,2,0,2,2,1,1,0,0,1,1,0,2,2,2,0,1,0,1,0,0,1,0,2,1,2,2,0,0,2,0,0,2,0,2,1,1,1,1,0,0,1,0,1,0,1,0,2,2,1,1,2,1,2,0,2,1,0,2,2,0,2,2,0,2,2,2,0,1,2,0,2,2,2,0,1,0,0,2,2,1,1,2,1,2,2,0,2,2,2,2,0,0,0,1,0,2,0,0,2,1,2,0,2,2,2,2,2,2,1,2,0,2,2,2,2,1,1,0,0,1,2,0,2,0,2,0,2,2,0,1,2,1,2,0,2,2,1,2,1,0,0,1,2,1,0,2,2,1,1,1,2,1,1,2,1,0,2,2,0,0,0,2,1,2,2,0,1,0,0,2,1,1,1,0,1,1,2,2,1,1,0,0,1,1,0,2,0,2,1,0,0,1,2,2,1,0,2,2,1,1,0,1,0,0,0,0,1,1,1,1,1,0,2,1,0,2,2,0,2,1,1,0,2,1,1,1,2,2,2,2,2,2,1,1,1,2,0,2,2,2,1,1,1,0,2,1,2,1,0,1,1,0,0,0,2,1,2,2,1,1,2,0,1,0,2,0,0,2,2,1,0,2,1,2,0,2,2,2,2,0,0,0,1,0,2,1,1,0,2,1,2,2,1,2,2,1,0,1,2,2,0,1,0,1,2,2,1,1,1,0,0,0,1,2,2,1,2,2,0,2,2,1,0,0,2,0,1,1,2,1,0,0,0,1,2,0,0,0,0,1,1,1,2,1,2,2,1,2,2,2,1,1,2,2,2,2,1,2,0,0,0,2,0,2,1,2,0,1,1,1,0,0,2,2,1,1,0,1,0,0,1,0,1,0,2,0,2,0,1,2,2,1,2,1,1,1,0,1,0,0,2,0,1,1,2,2,2,1,1,0,1,2,2,2,0,2,2,0,1,1,1,1,1,2,0,0,2,2,2,0,0,0,1,1,2,0,2,1,0,1,1,2,1,1,2,2,2,2,2,2,0,0,2,1,2,2,2,1,2,0,0,2,1,1,0,1,0,2,0,1,2,2,0,0,0,2,0,1,0,1,2,1,0,1,2,2,1,0,0,1,1,0,2,2,0,1,2,1,1,0,1,1,2,1,2,2,1,0,2,0,2,1,0,0,2,2,1,1,0,0,1,1,0,0,2,0,0,2,0,2,0,2,1,1,2,1,0,0,0,0,2,0,0,1,1,2,0,0,2,1,1,2,0,2,1,1,1,2,1,2,1,2,0,1,2,2,2,1,2,2,1,1,2,0,2,1,0,1,2,1,1,0,2,1,2,0,1,1,0,0,0,2,1,0,1,0,0,0,1,2,0,0,1,0,0,2,2,0,2,1,0,0,1,1,2,2,2,0,1,1,0,1,0,2,0,0,0,2,0,1,0,0,0,1,0,2,2,0,1,1,1,1,0,0,2,1,2,0,0,0,1,1,2,2,0,0,0,1,2,1,0,1,1,2,1,1,0,0,2,2,2,0,1,0,0,2,1,0,1,0,0,0,2,1,2,1,0,2,0,0,1,2,2,1,2,1,2,0,0,1,1,0,1,1,1,1,2,2,1,2,0,2,1,0,0,0,2,2,2,0,1,2,1,1,0,1,2,1,0,0,0,2,0,0,1,2,2,0,0,1,0,0,1,0,2,1,0,2,2,2,0,2,1,1,2,0,1,1,1,1,1,1,1,1,0,2,0,2,2,2,2,2,0,2,1,1,0,1,0,0,1,0,0,0,2,1,2,2,2,1,0,1,0,2,2,0,0,0,1,2,0,2,2,1,1,1,0,2,2,0,2,2,0,1,2,2,0,1,1,1,1,2,2,0,2,2,2,2,1,1,0,2,1,0,0,1,1,0,0,0,0,1,0,2,1,2,0,1,0,2,1,2,2,2,2,0,2,1,0,2,0,2,0,2,2,0,0,2,0,2,1,2,2,0,0,1,2,0,1,1,2,0,0,2,0,1,0,0,2,0,1,2,2,1,0,2,2,1,0,1,1,0,1,1,1,0,0,1,0,2,0,2,2,2,2,1,0,2,2,0,2,0,0,0,2,0,0,2,0,2,1,1,2,1,1,0,1,0,1,1,2,0,2,1,0,0,0,2,0,2,0,0,2,1,0,0,0,0,0,1,0,1,1,1,1,1,1,2,0,1,2,1,0,1,0,2,2,2,2,0,2,0,0,0,1,1,0,1,1,0,2,0,2,2,1,0,1,0,1,0,0,1,1,1,1,1,2,1,0,1,2,1,2,2,0,1,0,1,2,0,1,1,2,0,0,2,0,2,0,0,1,2,2,2,0,0,2,0,1,1,2,2,0,0,2,1,1,0,1,1,0,2,0,0,2,2,0,0,2,0,1,2,1,2,0,2,1,1,1,0,2,0,0,2,2,2,2,2,1,2,0,2,1,1,2,2,2,0,0,1,0,0,2,2,2,1,1,1,2,1,2,2,2,0,1,0,0,1,1,0,1,1,2,0,2,1,1,0,1,1,1,0,0,1,1,1,0,1,1,2,0,0,0,2,2,0,0,0,0,2,1,2,1,1,1,2,1,1,0,0,0,0,2,1,2,1,0,1,2,2,0,0,0,2,2,0,0,1,0,0,1,1,2,1,2,1,0,1,1,1,1,2,1,1,2,0,1,2,1,0,2,2,2,0,0,2,2,0,0,2,1,0,0,2,2,1,2,0,0,0,0,2,1,0,1,1,0,2,1,2,1,2,1,2,1,2,2,1,2,0,2,2,2,1,1,1,2,1,2,2,2,1,1,2,1,1,2,1,2,1,2,2,0,2,2,1,2,1,2,2,2,0,0,0,1,1,0,2,1,0,1,1,2,1,0,2,1,0,1,0,0,2,2,1,2,1,0,1,1,0,1,1,2,2,0,0,2,0,0,0,2,0,2,1,1,2,2,1,0,0,2,1,0,2,2,1,1,2,1,2,2,2,2,0,1,1,1,2,0,2,0,0,1,2,0,2,2,0,2,2,0,0,2,1,2,1,1,0,2,2,2,1,2,2,0,0,0,0,2,0,1,1,2,1,1,1,2,2,1,0,1,1,1,1,0,1,1,2,1,0,2,0,2,0,1,2,2,0,1,1,2,1,2,0,2,1,0,1,0,1,2,1,2,0,2,1,2,1,0,1,1,1,0,1,0,0,2,0,0,2,2,0,0,2,0,2,2,0,0,2,2,0,2,1,2,0,1,0,2,1,1,2,1,2,0,2,1,2,1,1,2,2,1,0,1,0,1,1,1,1,0,0,0,2,0,0,0,0,0,2,1,2,0,1,1,2,0,2,2,0,2,0,1,1,1,0,0,2,1,1,2,0,1,2,0,0,2,0,0,2,0,1,2,2,2,2,2,0,1,0,2,2,1,1,2,2,2,1,0,2,2,2,2,1,0,0,2,2,1,1,1,1,1,1,2,2,0,2,2,1,1,2,0,1,0,1,2,2,0,2,2,2,0,2,1,1,1,2,0,0,0,1,2,0,1,0,1,0,1,1,2,2,1,0,0,2,0,1,2,0,0,1,2,1,1,2,2,1,0,0,0,0,2,2,0,2,0,0,1,0,2,0,2,1,1,1,0,2,2,0,0,0,1,0,1,0,1,0,2,1,2,0,1,2,2,0,0,0,0,0,0,2,0,2,1,0,2,1,1,1,2,0,1,1,2,1,0,1,2,0,2,1,2,0,0,1,1,0,1,1,2,0,2,2,0,2,1,0,0,2,2,0,2,1,2,1,1,1,1,2,2,0,1,2,2,0,2,1,1,1,2,0,0,1,0,0,0,2,1,1,0,0,0,1,0,0,2,2,0,1,1,0,2,1,2,2,0,0,2,2,0,0,2,2,0,0,1,1,1,0,0,0,1,2,0,0,0,1,0,1,2,2,2,1,1,1,1,0,2,2,1,1,1,0,2,0,2,0,2,1,2,2,1,2,1,0,1,1,2,1,2,2,1,0,1,1,0,1,2,1,0,0,0,0,0,2,1,2,0,2,0,1,0,2,1,0,0,2,0,1,2,0,2,2,1,1,1,0,0,2,0,1,1,1,1,2,0,1,1,0,0,2,0,0,1,1,0,0,0,0,1,1,1,0,1,2,1,2,1,1,2,2,2,1,1,0,2,2,0,2,2,2,0,2,0,1,1,0,1,2,1,2,1,1,2,0,0,1,2,1,1,0,1,2,1,2,2,1,2,1,1,0,2,2,1,0,2,0,1,2,1,1,2,0,1,2,2,1,2,0,1,2,1,1,2,0,2,1,1,0,2,2,2,0,2,0,1,1,0,0,1,0,1,2,2,1,1,0,1,1,1,1,1,2,2,0,2,1,1,1,1,0,1,0,1,1,0,0,1,0,1,2,2,1,2,0,1,2,1,0,0,0,1,0,0,1,2,1,1,0,2,0,0,0,0,0,1,0,1,2,1,2,2,2,0,2,1,1,2,2,1,0,1,0,0,1,1,2,1,2,0,1,2,2,2,0,2,2,0,0,2,1,2,1,2,1,0,2,2,0,0,1,0,1,1,0,0,0,0,0,2,2,2,0,1,2,0,1,1,2,1,0,1,2,0,2,2,2,1,2,2,1,1,2,0,2,1,1,0,2,1,1,1,2,1,2,1,1,2,1,2,2,1,0,0,2,0,0,1,0,2,0,2,0,2,1,0,1,2,1,0,1,2,1,1,0,2,2,1,2,1,1,0,2,2,2,2,0,2,1,0,2,1,2,2,0,1,1,1,0,1,2,1,2,0,1,2,2,0,2,2,2,0,1,1,0,2,1,0,0,2,1,0,1,0,0,1,1,1,1,2,0,1,0,1,1,2,2,2,0,0,2,1,1,1,2,2,0,0,0,0,2,0,1,1,1,2,0,0,1,1,1,2,0,0,1,0,2,0,0,2,2,1,2,1,1,2,2,2,2,1,2,2,1,2,1,1,0,1,1,1,1,2,1,1,2,2,2,1,1,1,0,0,0,0,0,1,1,2,1,1,0,1,1,2,2,0,1,2,2,1,2,1,0,1,2,1,0,2,1,1,1,2,2,1,1,0,0,0,1,1,2,1,0,2,1,0,1,2,1,1,1,1,2,2,0,2,1,1,1,1,2,0,0,1,1,2,1,2,0,2,1,0,0,0,0,1,2,0,1,2,0,0,1,1,1,2,2,2,2,2,1,2,0,0,1,0,0,2,0,1,0,2,0,1,2,1,1,1,1,2,0,2,0,2,0,0,1,2,2,1,1,1,1,1,2,1,2,0,0,2,1,2,1,1,1,2,2,2,1,2,0,2,1,2,1,2,1,2,1,2,2,2,2,1,1,2,0,0,0,2,0,2,2,0,1,0,1,2,1,1,0,0,1,1,2,2,0,1,1,2,2,1,2,0,1,2,1,0,2,2,1,0,1,0,1,1,0,2,2,2,1,2,0,2,2,2,2,2,1,0,1,1,2,1,2,1,2,0,0,0,0,2,0,2,2,1,1,1,1,2,2,0,0,0,2,0,2,1,0,0,1,0,1,2,1,0,1,0,2,0,2,0,0,2,2,0,0,1,2,1,0,1,0,2,1,0,2,2,2,2,2,2,0,0,1,2,2,2,2,0,1,0,2,1,2,2,2,0,2,2,2,1,1,2,2,1,0,0,1,1,2,1,0,0,0,0,0,2,0,0,0,1,0,2,0,2,2,1,2,2,2,0,0,2,1,1,2,1,2,2,0,0,2,2,2,2,0,0,0,0,0,0,2,0,2,2,1,0,0,1,0,2,2,1,0,2,2,0,1,0,2,1,0,0,2,0,0,2,1,2,2,2,0,0,1,0,0,2,0,2,1,2,2,2,1,1,1,2,1,2,2,2,2,0,1,0,2,1,2,0,2,1,0,2,0,1,1,0,1,1,2,2,0,0,2,1,0,2,0,2,1,2,2,1,2,1,2,1,2,2,2,0,2,1,2,2,1,0,2,0,0,1,0,2,0,1,1,1,2,2,2,2,2,0,1,1,1,1,2,1,0,0,2,2,1,2,2,2,0,1,2,1,1,1,2,2,0,1,1,2,2,0,0,0,0,0,2,1,0,1,0,0,0,0,1,2,1,1,0,2,1,2,1,0,0,0,0,1,2,1,0,0,0,0,1,2,0,0,1,2,2,1,2,2,2,2,0,0,0,2,0,0,2,0,2,1,1,1,0,0,0,2,1,0,2,1,0,2,0,2,2,0,0,0,0,2,1,1,1,0,1,2,2,1,0,0,0,1,1,0,0,1,0,2,1,2,1,1,2,2,2,2,2,2,1,0,2,2,2,1,2,1,2,1,0,2,1,0,1,1,1,1,0,0,2,1,0,1,0,1,0,1,1,1,1,1,2,0,0,2,0,1,1,0,1,1,1,2,1,0,0,1,2,0,1,1,0,2,1,1,2,1,0,1,2,0,1,1,0,1,1,0,2,2,1,0,1,1,0,0,0,2,2,2,1,0,2,0,1,0,2,2,1,2,0,0,1,2,1,0,1,0,1,2,2,2,2,1,2,1,0,2,1,2,2,2,2,2,0,2,2,0,1,1,2,2,2,0,2,2,2,0,0,2,1,1,1,0,0,1,0,0,2,1,1,1,0,1,0,0,0,2,0,0,1,1,1,2,0,1,1,0,1,2,0,1,2,0,2,2,2,1,0,2,2,2,1,0,0,2,2,2,0,2,0,2,1,1,0,1,0,0,1,2,1,1,2,1,1,0,2,0,0,1,1,0,2,1,2,1,1,1,2,0,2,1,0,1,0,1,0,1,0,1,2,0,1,0,0,2,2,1,2,0,0,2,1,2,1,2,2,0,1,1,0,1,1,2,0,0,1,2,0,0,0,2,0,2,2,0,0,2,1,2,2,2,0,0,1,1,2,2,0,1,0,1,0,0,0,0,0,1,0,0,0,1,1,0,2,2,1,0,1,1,1,1,2,0,0,1,0,2,1,0,2,1,1,0,1,1,0,1,2,2,0,0,1,1,2,0,2,1,0,2,2,0,2,1,0,0,1,0,0,1,0,2,0,2,0,0,1,0,0,1,2,0,1,1,1,2,0,0,0,0,2,2,2,0,1,0,1,1,0,0,2,2,0,2,0,1,2,1,1,1,0,1,0,2,0,1,2,0,2,2,0,1,1,1,2,1,1,0,1,2,2,0,1,0,1,0,1,2,1,1,0,0,2,1,2,2,2,0,1,2,0,2,1,1,0,2,1,2,1,2,0,2,0,0,1,0,1,0,1,1,0,1,0,0,1,2,2,2,2,2,2,2,1,2,2,1,2,0,1,0,0,0,1,0,2,2,1,0,1,1,0,2,2,1,0,2,2,1,1,0,0,0,1,2,2,1,2,0,2,0,1,0,2,2,0,0,2,0,1,2,2,1,1,2,2,1,1,1,2,0,0,0,0,2,0,0,1,1,2,1,1,1,1,0,0,1,1,1,0,2,0,0,1,1,2,2,2,0,0,1,0,0,2,1,2,1,2,0,1,2,2,0,2,1,1,0,0,0,2,0,2,0,1,2,0,1,2,1,0,1,1,0,0,0,1,2,1,0,2,0,2,0,0,1,1,0,0,0,1,1,0,1,2,1,0,2,1,1,0,1,1,2,1,1,1,0,2,2,2,1,0,1,0,1,2,1,2,1,2,0,0,2,2,1,0,2,2,2,2,2,0,1,0,1,1,2,1,1,2,1,1,1,2,1,1,2,1,0,0,2,2,0,0,1,1,2,1,1,0,0,0,2,0,2,2,1,0,2,0,0,1,2,1,2,2,1,2,0,0,2,0,0,0,2,2,1,0,1,2,2,1,1,1,1,1,1,1,1,2,1,0,2,0,0,0,0,1,0,0,1,2,1,2,2,2,0,2,2,0,1,2,0,1,0,2,0,2,1,1,1,0,2,1,2,1,2,0,1,0,2,2,2,0,1,1,1,2,2,2,0,1,0,2,2,2,2,0,0,0,2,1,2,2,1,2,0,1,1,1,0,0,1,1,1,2,1,1,2,2,2,0,0,0,2,2,1,1,0,2,1,2,1,1,2,1,1,2,0,1,1,1,1,2,2,2,2,2,1,1,0,0,2,1,2,0,2,2,1,1,1,2,2,0,1,2,0,0,0,0,0,2,0,2,2,1,2,0,2,1,0,1,2,2,2,0,2,2,2,2,1,2,1,2,2,0,0,2,2,0,1,2,0,2,1,0,2,1,1,2,1,2,2,1,2,2,2,0,1,1,0,0,1,0,2,2,0,1,2,1,0,2,2,0,1,0,2,2,1,1,0,2,1,1,2,2,1,2,2,1,0,1,2,0,1,1,1,0,2,0,0,2,2,0,2,1,0,2,0,1,0,0,1,0,1,0,2,2,1,1,0,1,0,1,0,1,2,2,2,2,1,2,1,0,0,2,1,0,0,0,1,2,2,0,1,1,2,2,0,1,0,0,1,0,1,1,1,2,0,2,0,0,1,1,1,0,1,1,2,2,2,1,0,0,2,2,0,2,2,1,2,0,0,2,2,0,0,2,2,0,0,1,0,2,1,0,1,1,0,2,0,0,0,0,2,1,1,2,0,0,2,1,0,0,1,2,1,1,0,0,0,2,2,2,1,2,1,0,1,1,1,0,1,0,0,2,0,0,1,0,2,2,2,2,2,1,1,0,0,0,1,1,0,2,1,1,1,2,1,0,0,1,0,2,2,2,0,1,1,0,1,1,2,0,1,2,1,0,2,1,0,0,2,1,0,2,1,2,2,1,2,0,2,2,0,0,1,0,2,2,1,2,1,2,2,1,1,0,0,2,2,1,1,2,2,1,2,0,0,0,2,2,2,0,1,0,2,1,2,2,2,2,2,1,0,1,0,1,0,0,0,1,1,0,2,1,2,0,1,0,1,1,0,0,1,1,0,2,0,0,1,1,2,0,2,1,0,0,2,0,1,2,0,0,0,1,1,0,2,0,2,0,2,0,0,1,1,0,0,0,2,0,2,1,0,1,0,1,0,1,2,1,1,0,0,1,2,1,0,2,0,1,1,1,2,2,2,2,0,1,0,0,1,2,2,2,2,1,0,0,0,2,2,1,1,1,2,0,1,0,0,1,1,1,1,1,2,0,2,1,1,2,2,1,1,2,2,2,0,2,2,2,1,1,2,1,1,0,1,2,0,1,2,0,2,0,2,2,0,2,1,0,2,0,1,1,0,2,1,1,2,0,1,1,1,2,1,2,1,2,2,1,1,0,0,2,2,1,2,0,1,1,2,1,1,1,1,0,1,0,2,0,1,1,1,0,0,0,1,1,1,1,0,0,2,1,2,2,1,1,2,1,0,1,2,1,1,1,1,0,0,1,0,0,0,0,0,1,0,1,1,0,2,0,2,1,1,0,2,2,2,0,2,1,2,2,1,1,1,1,1,0,0,0,1,2,2,2,0,0,0,0,2,1,0,1,0,2,1,0,1,0,1,2,0,1,0,2,1,1,1,0,2,1,2,0,1,1,1,0,0,0,0,2,0,0,2,0,2,1,0,1,0,0,0,1,1,0,2,1,2,1,2,2,0,1,2,0,2,1,1,0,1,1,1,2,0,0,1,2,1,2,0,1,2,1,2,0,1,2,1,0,1,2,1,0,1,1,1,0,1,1,2,0,1,0,0,1,1,1,1,1,0,2,2,0,2,2,0,1,1,2,1,2,0,2,1,0,2,1,1,1,2,0,0,2,1,2,2,2,2,2,1,0,2,2,0,1,1,0,2,2,1,1,0,2,1,2,0,0,2,1,1,2,0,0,0,0,2,2,0,1,1,0,2,2,1,2,1,1,0,2,2,0,1,2,1,2,1,0,1,1,0,0,2,2,2,0,0,2,2,0,0,0,0,0,0,1,1,0,2,0,0,2,0,2,0,0,0,2,1,2,2,1,0,2,2,1,2,2,0,2,0,1,0,0,1,2,1,0,1,0,0,1,0,0,0,1,1,1,2,2,2,1,0,2,2,2,0,2,1,2,1,2,0,1,1,0,0,0,2,2,1,1,1,2,0,2,1,1,1,0,0,1,2,2,0,0,0,1,1,2,1,2,0,2,1,2,2],
25000000)) #1

            