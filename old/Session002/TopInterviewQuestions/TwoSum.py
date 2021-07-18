class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        u=dict()
        for i in range(len(nums)):
            u[nums[i]]=i

        for i in range(len(nums)):
            dif=target-nums[i]
            if dif in u and  u[dif]!=i:
                return [i, u[dif]]
        return []

if __name__ =="__main__":
    c=Solution()
    nums = [2, 7, 11, 15]
    target = 18
    print(c.twoSum(nums,target))
