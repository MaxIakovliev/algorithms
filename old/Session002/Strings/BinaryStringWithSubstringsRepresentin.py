class Solution:
    """
    https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/
    """
    def queryString(self, S: str, N: int) -> bool:
        for i in range(1,N+1):
            if str(''.join(bin(i)[2:])) not in S:
                return False
        return True
if __name__ == "__main__":
    c=Solution()
    print(c.queryString("0110",3))#True
    print(c.queryString("0110",4))#False
    print(c.queryString("1",1))#True
    print(c.queryString("1",1))#True
        