class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return 0
        res=self.doCheck(n,0)
        
        return res

    def doCheck(self, n, res):
        if n==1:
            return res
        if n%2==0:
            
            return  self.doCheck(n/2,  res+1)
        else:
            res= min(self.doCheck(n-1,res+1),self.doCheck(n+1, res+1))
            return res
        return res
            
            
        
        


if __name__=="__main__":
    c=Solution()
    print(c.integerReplacement(8)) #3
    print(c.integerReplacement(7)) #4
    print(c.integerReplacement(65535)) #4
