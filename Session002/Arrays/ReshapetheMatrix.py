class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        res = [[0]*c for _ in range(r)]
        i1 = 0
        j1 = 0
        count=0
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if j1 >= c:
                    j1 = 0
                    i1 += 1
                    if i1>r*c:
                        return nums

                res[i1][j1] = nums[i][j]
                count+=1
                j1 += 1
        if count<r*c:
            return nums
        return res


if __name__ == "__main__":
    cc = Solution()
    nums = [[1, 2], [3, 4]]
    r = 1
    c = 4
    print(cc.matrixReshape(nums, r, c)) #[[1,2,3,4]]
    r = 4
    c = 1
    print(cc.matrixReshape(nums, r, c)) #[[1,2],[3,4]]

    nums=[[1,2,3,4]]
    r=2
    c=2
    print(cc.matrixReshape(nums, r, c)) #[[1,2],[3,4]]
    
