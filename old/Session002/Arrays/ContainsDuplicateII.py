class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)<=1:
            return False
        d={}
        for i in range(len(nums)):
            if nums[i] in d and abs(i-d[nums[i]])<=k:
                return True
            elif nums[i] not in d:
                d[nums[i]]=i
            else:
                d[nums[i]]=i
                    
        return False
    
if __name__=="__main__":
    c=Solution()
    print(c.containsNearbyDuplicate([1,2,3,1],3)) #True
    print(c.containsNearbyDuplicate([1,0,1,1],1)) #True
    print(c.containsNearbyDuplicate([1,2,3,1,2,3],2)) #False

        
                