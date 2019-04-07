class Solution:
    """
    https://leetcode.com/problems/binary-gap/
    """
    def binaryGap(self, N: int) -> int:
        max_len=0
        b=bin(N)[2:]
        start=-1
        for i in range(len(b)):
            if b[i]=='1':
                if start==-1:
                    start=i
                else:
                    max_len=max(i-start,max_len)
                    start=i
        return max_len

if __name__ == "__main__":
    c=Solution()
    print(c.binaryGap(22))#2
    print(c.binaryGap(5))#2
    print(c.binaryGap(6))#1
                    

        