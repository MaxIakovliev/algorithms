class Solution:
    def bitwiseComplement(self, N: int) -> int:
        res=list(bin(N))
        for i in range(2, len(res)):
            if res[i]=='1':
                res[i]='0'
            else:
                res[i]='1'
        return int(''.join(res),2)
if __name__ == "__main__":
    c=Solution()
    print(c.bitwiseComplement(5))#2
    print(c.bitwiseComplement(10))#5
    print(c.bitwiseComplement(7))#0
