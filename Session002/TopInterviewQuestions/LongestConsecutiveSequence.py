class Solution:
    """
    https://leetcode.com/problems/longest-consecutive-sequence/description/
    """
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSoFar=0
        u=set(nums)
        while len(u)>0:
            item=u.pop()
            cur=item
            u.remove(cur)
            count=1
            cur+=1
            while cur in u:
                u.remove(cur)
                cur+=1
                count+=1
            
            cur=item-1
            while cur in u:
                u.remove(cur)
                cur-=1
                count+=1
            maxSoFar=max(maxSoFar, count)
        return maxSoFar



        