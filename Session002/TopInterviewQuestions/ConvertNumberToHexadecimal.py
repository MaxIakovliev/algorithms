class Solution(object):
    """
    https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/
    """
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return "0"
        if num<0:
            return self.toHex(num+2**32)
        digits = "0123456789abcdef"
        reminder=(int)(num %16)
        rest=num//16
        if rest==0:
            return digits[reminder]
        return self.toHex(rest)+digits[reminder]


if __name__=="__main__":
    c=Solution()
    for i in range(27):
        print(c.toHex(i))
    print(c.toHex(-2))
