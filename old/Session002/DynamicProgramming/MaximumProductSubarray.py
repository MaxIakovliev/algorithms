class Solution:
    """
    https://leetcode.com/problems/maximum-product-subarray/
    """
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minVal=[0]*len(nums)
        maxVal=[0]*len(nums)
        res=nums[0]
        minVal[0]=nums[0]
        maxVal[0]=nums[0]
        for i in range(1, len(nums)):
            maxVal[i]=max(max(maxVal[i-1]*nums[i],minVal[i-1]*nums[i]), nums[i])
            minVal[i]=min(min(maxVal[i-1]*nums[i],minVal[i-1]*nums[i]), nums[i])
            res=max(maxVal[i],res)
        
        return res

    def maxProductOptimized(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=nums[0]
        minVal=nums[0]
        maxVal=nums[0]
        for i in range(1, len(nums)):
            prevMaxVal=maxVal
            prevMinVal=minVal
            maxVal=max(max(prevMaxVal*nums[i],prevMinVal*nums[i]), nums[i])
            minVal=min(min(prevMaxVal*nums[i],prevMinVal*nums[i]), nums[i])
            res=max(maxVal,res)
        
        return res

    def maxProductDP_version(self, nums):
        n=len(nums)
        f=[0]*2
        f[0],f[1]=nums[0],nums[0]
        max_val=nums[0]
        for i in range(1, n):
            ff=[0]*2
            if nums[i]==0:
                ff[0],ff[1]=0,0
            elif nums[i]>0:
                ff[0]=max(nums[i],nums[i]*f[0])
                ff[1]=min(nums[i],nums[i]*f[1])
            else:
                ff[0]=max(nums[i],nums[i]*f[1])
                ff[1]=min(nums[i],nums[i]*f[0])
            max_val=max(max_val,ff[0])
            f=ff
        return max_val




if __name__ =="__main__":
    c=Solution()
    print(c.maxProductDP_version([2,3,-2,4])) #6
    print(c.maxProductDP_version([-2,0,-1]))
    print(c.maxProductDP_version([-2,3,-4]))
            

            