class Solution:
    """
    https://leetcode.com/problems/partition-equal-subset-sum/
    
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

    Each of the array element will not exceed 100.
    The array size will not exceed 200.

 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].

 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.


solution:
https://leetcode.com/problems/partition-equal-subset-sum/discuss/286594/python-dynamic-programming

    """
    def canPartition(self, nums: 'List[int]') -> bool:
        num_sum=sum(nums)
        if num_sum %2!=0:
            return False
        dp=[0]*(num_sum+1)
        dp[0]=1
        for num in nums:
            for i in range(num_sum,-1,-1):
                if dp[i]==1:
                    dp[num+i]=1
            if dp[num_sum//2]==1:
                return True
        return False



        

        