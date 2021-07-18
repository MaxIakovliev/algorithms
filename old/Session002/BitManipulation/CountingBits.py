class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res=[]
        for i in range(0,num+1):
            res.append(self.count(i))
        return res
    
    def count(self, n):
        res=0
        b=bin(n)
        for i in range(2,len(b)):
            if (int)(b[i])==1:
                res+=1
        return res

    def countBits_DP_approach(self, num):
        dp=[0 for i in range(num+1)]
        dp[0]=0
        
        if num>=1:
            dp[1]=1

        nearest=2
        curr=2
        while curr<=num:
            if self.isNumberPowerOfTwo(curr):
                nearest=curr

            dp[curr]=1+dp[curr-nearest]
        return dp

    def isNumberPowerOfTwo(self, n):
        return  (n & (n-1))==0



if __name__ =="__main__":
    c=Solution()
    print(c.countBits(5))
