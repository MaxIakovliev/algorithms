class Solution:
    """
    https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
    """
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==0:
            return []
        u=set()
        res=[]
        for i in range(len(nums)):
            if nums[i] in u:
                res.append(nums[i])
            else:
                u.add(nums[i])
        return res
if __name__=="__main__":
    c=Solution()
    print(c.findDuplicates([4,3,2,7,8,2,3,1])) #[2,3]


        