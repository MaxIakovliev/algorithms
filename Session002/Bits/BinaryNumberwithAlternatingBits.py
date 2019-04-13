class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b=bin(n)
        for i in range(3,len(b)):
            if b[i]==b[i-1]:
                return False
        return True
if __name__ == "__main__":
    c=Solution()
    print(c.hasAlternatingBits(5))#true
    print(c.hasAlternatingBits(7))#false
    print(c.hasAlternatingBits(11))#false
    print(c.hasAlternatingBits(10))#True
        
        