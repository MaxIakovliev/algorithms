class Solution:
    """
    https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/
    """
    def maxSumTwoNoOverlap(self, A: 'List[int]', L: int, M: int) -> int:
        def find_best_sum(arr, l,m):
            front_best=0
            res=0
            for i in range(l+m, len(arr)):
                front=arr[i-m]-arr[i-m-l]
                back=arr[i]-arr[i-m]
                front_best=max(front_best,front)
                res=max(res,front_best+back)
            return res

        A2=[0]+A[:]
        for i in range(1,len(A2)):
            A2[i]=A2[i]+A2[i-1]
        
        return max(find_best_sum(A2,L,M), find_best_sum(A2, M,L))
if __name__ == "__main__":
    c=Solution()
    # print(c.maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4], 1,  2))#20
    # print(c.maxSumTwoNoOverlap([2,1,5,6,0,9,5,0,3,8], L = 4, M = 3))#31
    print(c.maxSumTwoNoOverlap([1,0,1], L = 1, M = 1))#2

        