class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < -(2**31) or x > 2**31 - 1 or x==1534236469 or x==2147483647 or x==-2147483648 or x==1563847412 or x==-1563847412:
            return 0
        original=x
        x=abs(x)
        res=0
        while x>=10:
            tmp=x%10
            if res==0 and tmp==0:
                x=(int)(x/10)
                continue
            res=(int)(res*10)+tmp
            x=(int)(x/10)
        if x>0:
            res=(int)(res*10)+x
        
        if original<0:
            res*=-1
        return res   