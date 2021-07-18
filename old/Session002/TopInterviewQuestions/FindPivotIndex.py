class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return -1
        total=0
        for n in nums:
            total+=n
        left=0
        for i in range(0,len(nums)):
            if i>0:
                left+=nums[i-1]
            if left==total-nums[i]-left:
                return i
        return -1

if __name__=="__main__":
    c=Solution()
    print(c.pivotIndex([1, 7, 3, 6, 5, 6]))
    print(c.pivotIndex([-1,-1,-1,0,1,1]))