class Solution(object):
    """
    https://leetcode.com/problems/next-greater-element-i/description/
    """
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        pos={}
        for i in range(len(nums)):
            pos[nums[i]]=i
        for i in range(len(findNums)):
            val=-1
            for j in range(pos[findNums[i]],len(nums)):
                if nums[j]>findNums[i]:
                    val=nums[j]
                    break
            res.append(val)
        return res

if __name__=="__main__":
    c=Solution()
    print(c.nextGreaterElement([4,1,2], [1,3,4,2]))
             
                

            