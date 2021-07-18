class Solution:
    def transpose(self, a):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(a)
        n = len(a[0])
        res = [[0]*m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][i]=a[i][j]
        return res
if __name__ == "__main__":
    c=Solution()
    print(c.transpose([[1,2,3],[4,5,6],[7,8,9]])) #[[1,4,7],[2,5,8],[3,6,9]]
    print(c.transpose([[1,2,3],[4,5,6]])) #[[1,4],[2,5],[3,6]]
