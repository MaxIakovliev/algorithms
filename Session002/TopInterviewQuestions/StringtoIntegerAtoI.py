class Solution:
    """
    https://leetcode.com/problems/string-to-integer-atoi/description/
    """
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        res=0
        minVal=(pow(2,31))*-1
        maxVal=pow(2,31)-1
        metSign=False
        negative=False
        metDigit=False
        for i in range(len(s)):
            if s[i]>='a' and s[i]<='z' or s[i]>='A' and s[i]<='Z' or s[i] in ['.',',','!','@','#','$','%','%','^','&','*','(',')']:
                break
            if ord(s[i])-ord('0')>=0 and ord(s[i])-ord('0')<=9:
                if i>0 and s[i-1] not in ['-','+']and (ord(s[i-1])-ord('0')<0 or ord(s[i-1])-ord('0')>9) and (metDigit or metSign):
                    break
                res*=10
                res+=(ord(s[i])-ord('0'))
                metDigit=True
            elif s[i] in ['-','+']:
                if metSign or metDigit:
                    break
                metSign=True
                if s[i]=='-':
                    negative=True
        if negative:
            res=res*-1

        if res< minVal:
            return minVal
        if res>maxVal:
            return maxVal
        return res
if __name__=="__main__":
    c=Solution()
    print("expected 0, res={0}".format(c.myAtoi("")))
    print("expected 1, res={0}".format(c.myAtoi("1")))
    print("expected 1, res={0}".format(c.myAtoi(" 1")))
    print("expected 1, res={0}".format(c.myAtoi(" 1 ")))
    print("expected 1, res={0}".format(c.myAtoi(" 1 a")))
    print("expected 1, res={0}".format(c.myAtoi(" 1 1 a")))
    print("expected 1, res={0}".format(c.myAtoi(" +1 1 a")))
    print("expected 1, res={0}".format(c.myAtoi(" -1 1 a")))
    print("expected -1, res={0}".format(c.myAtoi(" -1 1 a")))
    print("expected -11, res={0}".format(c.myAtoi(" -11 1 a")))
    print("expected 0, res={0}".format(c.myAtoi(" -s11 1 a")))
    print("expected 0, res={0}".format(c.myAtoi("- 234")))





