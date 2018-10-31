class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num:int=0
        for n in digits:
            num*=10
            num+=n
        num+=1
        
        res=[0]*len(str(num))
        step=len(res)-1
        while step>=0:
            res[step]=num%10
            num//=10
            step-=1
        return res
if __name__ =="__main__":
    c=Solution()
    print(c.plusOne([1,2,3]))
    print(c.plusOne([9,9,9]))


