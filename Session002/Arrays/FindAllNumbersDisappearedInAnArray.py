class Solution:
    """
    https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
    """
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==0:
            return []
        res=[]
        nums.sort()        
        for i in range(len(nums)):
            if i>0 and nums[i]-nums[i-1]>0:
                for v in  range(nums[i-1]+1,nums[i]):
                    if v!=nums[i-1] and v!=nums[i]:
                        res.append(v)
        return res

    def findDisappearedNumbers2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==0:
            return []

        res=set()
        for i in range(1,len(nums)+1):
            res.add(i)
        
        for i in range(len(nums)):
            if nums[i] in res:
                res.remove(nums[i])
        return list(res)

if __name__=="__main__":
    c=Solution()
    print(c.findDisappearedNumbers2([4,3,2,7,8,2,3,1]))
    print(c.findDisappearedNumbers2([1]))
    print(c.findDisappearedNumbers2([1,1]))
    print(c.findDisappearedNumbers([1,2]))
    print(c.findDisappearedNumbers2([1,1,1]))

            
