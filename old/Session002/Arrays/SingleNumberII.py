class Solution:
    """
    https://leetcode.com/problems/single-number-ii/description/
    """
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t={}
        for i in range(len(nums)):
            if nums[i] in t:
                t[nums[i]]+=1
            else:
                t[nums[i]]=1
                
            if t[nums[i]]==3:
                del t[nums[i]]
        
        res=0
        for key, val in t.items():
            res=key
        return res

if __name__=="__main__":
    c=Solution()
    print(c.singleNumber([2,2,3,2])) #3
    print(c.singleNumber([0,1,0,1,0,1,99])) #99

                