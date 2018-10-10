class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or  len(nums)==0:
            return 0
        j=0
        i=0
        minVal=float('inf')
        sum=0
        while i<len(nums):
            sum+=nums[i]
            i+=1
            while sum>=s:
                minVal=min(minVal, i-j)
                sum-=nums[j]
                j+=1
        if minVal==float('inf'):
            return 0
        return minVal

if __name__=="__main__":
    c=Solution()
    print(c.minSubArrayLen(7,[2,3,1,2,4,3])) #2
