class Solution(object):
    """
    https://leetcode.com/problems/happy-number/description/
    """
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def getNextNum(num:int)->(int):
            res=[]
            while num!=0:
                if num<=9:
                    res.append(num)
                    break

                res.append(num%10)
                num//=10
            val=0
            for cur in res:
                val+=(cur**2)
            return val

        def getNextNum2(num:int)->(int):
            val=0
            while num!=0:
                if num<=9:
                    val+=(num**2)
                    break

                val+=((num%10)**2)
                num//=10
            return val            
                

        u=set()
        if n==1:
            return True
        while n not in u:
            if n in u:
                return False
            u.add(n)
            n=getNextNum2(n)
            if n==1:
                return True
        return False

if __name__=="__main__":
    c=Solution()
    for i in range(100):
        print("{0} is {1}".format(str(i),str(c.isHappy(i))))
