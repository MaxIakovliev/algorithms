class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = 0
        cur = 0
        for i in range(len(nums)):
            if nums[i] != 1:
                mx = max(mx, cur)
                cur = 0
            elif nums[i] == 1:
                cur += 1

        mx = max(mx, cur)
        return mx

if __name__ == "__main__":
    c=Solution()
    print(c.findMaxConsecutiveOnes([1,1,0,1,1,1]))