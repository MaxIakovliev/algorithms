class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False

        reversedNum=0
        tmp=x
        count=0
        while tmp>0:
            n=tmp%10
            reversedNum=reversedNum*10+n
            tmp=(int)(tmp/10)
            count+=1

        count=(int)(count/2)
        i=0
        while(i< count):
            t1=x%10
            t2=reversedNum%10
            if t1!=t2:
                return False
            x=(int)(x/10)
            reversedNum=(int)(reversedNum/10)
            i+=1
        return True
if __name__ =="__main__":
    c=Solution()
    print(c.isPalindrome(1231))