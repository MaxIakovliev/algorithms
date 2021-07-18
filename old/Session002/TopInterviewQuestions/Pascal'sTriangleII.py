class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res=[]
        for i in range(1,rowIndex+2):
            tmp=[1]*i
            res.append(tmp)

        for i in range(2, len(res)):
            for j in range(1,len(res[i])-1):
                res[i][j]=res[i-1][j-1]+res[i-1][j]
        return res[rowIndex]


if __name__=="__main__":
    c=Solution()
    print(c.getRow(3))
