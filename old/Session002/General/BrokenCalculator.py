class Solution(object):
    """
    https://leetcode.com/problems/broken-calculator/
    """
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        ans = 0
        while Y > X:
            ans += 1
            if Y%2: Y += 1
            else: Y //= 2

        return ans + X-Y
        
if __name__=="__main__":
    c=Solution()
    print(f"res={c.brokenCalc(2,3)}")#2
    print(f"res={c.brokenCalc(5,8)}")#2
    print(f"res={c.brokenCalc(3,10)}")#3
    print(f"res={c.brokenCalc(1024,1)}")#1023
    print(f"res={c.brokenCalc(1,10000000)}")#1023
