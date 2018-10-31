class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        def highestOneBit(n):
            count=0
            for c in str(bin(n)):
                if c=="1":
                    return count
                count+=1
            return -1
        #-3 because number represent as "0b"some numnbers after it
        # -2 to substract 0b
        #-1 to substract leading 0
        mask=highestOneBit(num)-1
        num=~num #flip all bits
        return num&mask
if __name__=="__main__":
    c=Solution()
    print(c.findComplement(5))