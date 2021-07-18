class Solution:
    """
    https://leetcode.com/problems/first-missing-positive/description/
    """
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp=set()
        for i in range(len(nums)):
            if nums[i]>0:
                tmp.add(nums[i])

        for i in range(1,len(tmp)+1):
            if i not in tmp:
                return i

        return len(tmp)+1
        

            
                

        

if __name__=="__main__":
    c=Solution()
    print(c.firstMissingPositive([1,2,0])) #3
    print(c.firstMissingPositive([3,4,-1,1])) #2
    print(c.firstMissingPositive([7,8,9,11,12])) #1
