class Solution:
    def flipAndInvertImage(self, a):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(a)):
            halfLen = (int)(len(a[i])/2)
            j=0
            ln=len(a[i])
            if ln%2!=0:
                a[i][halfLen]=1-a[i][halfLen]
            while j<halfLen:
                t=a[i][j]
                a[i][j]=1-a[i][ln-1-j]
                a[i][ln-1-j]=1-t
               
                j+=1

        return a


if __name__ == "__main__":
    c = Solution()
    print(c.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]])) # [[1,0,0],[0,1,0],[1,1,1]]
    print(c.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]])) # [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
