class Solution(object):
    """
    https://leetcode.com/problems/continuous-subarray-sum/description/
    
    1. when there are two subsequent 0, whatever k is, we should return true, because 0*k=0;
    2. when k==0 and there are no two subsequent 0, return false;
    3. iterate through the array, sum+=nums[i], calculate the mod = sum%k, if the same mod has appeared before when i=j, then sum(nums(j...i])==n*k
    4. we put m[0]==-1 at the beginning, think nums = {1,1} and k = 2, sum(nums[0...1])%2=0, so this makes it apply the previous statement;
    5. we need to do the check "if (!( m[0]==-1 && i==0))", in case situations like nums={1} and k=1

    """
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        
        #Case 1 ----
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]==0:
                return True

        if k==0: #Case 2
            return False
                        
        m={}
        m[0]=-1
        _sum=0
        for i in range(len(nums)):
            _sum+=nums[i]
            _sum%=k
            if _sum in m:
                if not (m[0]==-1 and i==0):
                    return True
            m[_sum]=i
        return False

    def checkSubarraySum2(self, nums, k):
        """
        easy to understand solution
        """
        if not nums or len(nums)==0:
            return False

        presum=[0]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            presum[i]=presum[i-1]+nums[i-1]
        
        for i in range(len(nums)):
            for j in range(i+2,len(nums)+1):
                if k==0:
                    if presum[j]-presum[i]==0:
                        return True
                elif (presum[j]-presum[i])%k==0:
                    return True
        return False

if __name__ == "__main__":
    c=Solution()
    print(c.checkSubarraySum2([0,0],0))

        

        
        