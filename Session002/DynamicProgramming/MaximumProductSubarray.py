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




if __name__ =="__main__":
    c=Solution()
    print(c.maxProductOptimized([2,3,-2,4]))
    print(c.maxProductOptimized([-2,0,-1]))
    print(c.maxProductOptimized([-2,3,-4]))
            

            