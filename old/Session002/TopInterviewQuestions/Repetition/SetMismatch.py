class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        u=set()
        for n in nums:
            if n in u:
                res.append(n)
            else:
                u.add(n)
        for i in range(1, len(nums)+1):
            if i not in u:
                res.append(i)
                return res
        return res