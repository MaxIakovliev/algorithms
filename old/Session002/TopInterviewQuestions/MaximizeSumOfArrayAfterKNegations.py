class Solution:
    """
    https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
    """
    def largestSumAfterKNegations(self, arr: "List[int]", k: int) -> int:
        arr.sort()
        while k>0:
            arr[0]=arr[0]*(-1)
            arr.sort()
            k-=1
        res=0
        for item in arr:
            res+=item
        return res
if __name__ == "__main__":
    c=Solution()
    print(c.largestSumAfterKNegations([4,2,3],1))#5
    print(c.largestSumAfterKNegations([3,-1,0,2],3))#6
    print(c.largestSumAfterKNegations([2,-3,-1,5,-4],2))#13

        