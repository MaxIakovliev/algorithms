class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        total=(n)*(n+1)//2
        for i in range(0,n):
            total-=nums[i]
        return total

    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        x1 = nums[0] # For xor of all the elements in array
        x2 = 1 # For xor of all the elements from 1 to n+1
        for i in range(n):
            x1 ^= nums[i]
        for i in range(n+2):
            x2 ^= i
            return x1^x2
if __name__=="__main__":
    c=Solution()
    print(c.missingNumber2([3,0,1])) #2
    print(c.missingNumber2([6,4,2,3,5,7,0,1])) #8
