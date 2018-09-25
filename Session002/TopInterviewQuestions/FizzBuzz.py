class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        for i in range(1,n+1):
            c1=i %3==0
            c2=i %5==0
            if c1 and c2:
                res.append("FizzBuzz")
            elif c1:
                res.append("Fizz")
            elif c2:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
                