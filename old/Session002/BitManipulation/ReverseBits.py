import sys
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
         
        x=0
        for i in range(31,-1,-1):
            x |= (n & 1) << i
            n >>= 1
        return x

if __name__ == "__main__":
    c=Solution()
    print(c.reverseBits(43261596))#964176192 
    

