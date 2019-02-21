class Solution(object):
    """
    https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
    """
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        def getAllPrimesInRange(n):
            res=set()
            for i in range(2, n):
                canAdd=True
                for j in range(2,i):
                    if i%j==0:
                        canAdd=False
                        break
                if canAdd:
                    res.add(i)
            return res
        
        def countBitsInNumber(n):
            """
            great example on how to count bits in integer:
            https://stackoverflow.com/a/109045
            """
            count=0
            while n>0:
                if n&1==1:
                    count+=1
                n=n>>1
            return count

        primes= getAllPrimesInRange(32)
        result=0
        for i in range(L, R+1):
            count_bits=countBitsInNumber(i)
            if count_bits in primes:
                result+=1
        return result



if __name__=="__main__":
    c=Solution()
    print(c.countPrimeSetBits(6,10))
    print(c.countPrimeSetBits(10,15))
                    
        