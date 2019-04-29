class Solution:
    """
    https://leetcode.com/problems/single-element-in-a-sorted-array/
    """
    def singleNonDuplicate(self, nums: 'List[int]') -> int:
        n=len(nums)
        for i in range(0,n,2):
            if i+1<n and nums[i]!=nums[i+1]:
                return nums[i]
        return nums[-1]
if __name__ == "__main__":
    c=Solution()
    print(c.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))#2
    print(c.singleNonDuplicate([3,3,7,7,10,11,11]))#10