class Solution(object):
    """
    https://leetcode.com/problems/divide-two-integers/description/
    """
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        result=0
        data=0
        while data<=abs(dividend):
            data+=abs(divisor)
            result+=1

        if data>abs(dividend):
            result-=1
        if dividend<0 and divisor>0:
            return -result

        if dividend>0 and divisor<0:
            return -result

        return result 

if __name__=="__main__":
    c=Solution()
    print(c.divide(0,3))#3
    print(c.divide(10,3))#3
    print(c.divide(-10,3))#-3
    print(c.divide(10,-3))#-3

        