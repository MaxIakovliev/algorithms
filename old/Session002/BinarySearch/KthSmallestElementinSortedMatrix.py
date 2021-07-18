class Solution:
    
    def kthSmallest2(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        ln=len(matrix)
        lo=matrix[0][0]
        hi=matrix[ln-1][ln-1]
        while lo<=hi:
            mid=(int)((lo+hi)/2)
            count=self.lessEqual(matrix, mid)
            if count<k:
                lo=mid+1
            else:
                hi=mid-1
        return lo
    
    def lessEqual(self, matrix, val):
        res=0
        ln=len(matrix)
        i=ln-1
        j=0
        while( i>=0 and j<ln):
            if matrix[i][j]>val:
                i-=1
            else:
                res +=(i+1)
                j+=1
        return res

                

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        ln=len(matrix)
        row=0
        if k<=ln:
            return matrix[0][k-1]
        counter=1
        while True:
            cur=ln*counter
            if cur<=k and (ln*(counter+1))>=k:
                row=counter
                break
            else:
                counter+=1
        
        col=k-row*ln       

        if col>0:            
            return matrix[row][col-1]

        return matrix[row][col]

         
 


if __name__ =="__main__":
    matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
    c=Solution()
    # print(str(4)+"=>"+str(c.kthSmallest(matrix,4)))
    for i in range(1,10):
        print(str(i)+"=>"+str(c.kthSmallest2(matrix,i)))

    matrix=[[1,2],[1,3]]
    print(str(2)+"=>"+str(c.kthSmallest2(matrix,2)))

    