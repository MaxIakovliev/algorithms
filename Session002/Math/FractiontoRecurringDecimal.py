class Solution:
    """
    https://leetcode.com/problems/fraction-to-recurring-decimal/
    """
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = ''
        if numerator * denominator < 0:
            res += '-'

        integer, remainder = divmod(abs(numerator), abs(denominator))
        res += str(integer)

        if remainder:
            res += '.'
            remainders = {}
            while remainder:
                if remainder not in remainders:
                    remainders[remainder] = len(res)
                    integer, remainder = divmod(remainder * 10, abs(denominator))
                    res += str(integer)
                else:
                    index = remainders[remainder]
                    res = res[:index] + '(' + res[index:] + ')'
                    break
        return res  
    # def fractionToDecimal(self, numerator: int, denominator: int) -> str:
    #     fres=numerator/denominator
    #     s=str(fres)
    #     dot_idx=s.index('.')
    #     if len(s[dot_idx+1:])==1 and s[-1]=='0':
    #         return s[:dot_idx]
    #     d=[]
    #     u=set()
    #     mantissa=s[dot_idx+1:]
    #     for i in range(len(mantissa)):
    #         if len(d)==0:
    #             d.append(str(mantissa[i]))
    #         elif mantissa[i]== d[0]:
    #             count=0
    #             for j in range(i,len(mantissa)):
    #                 if count <len(d) and  mantissa[j]==d[count]:
    #                     count+=1
    #                 else:
    #                     break
    #             local_s="".join(d[:count])
    #             allow=True
    #             for k in u:
    #                 if len(k)==len(local_s):
    #                     allow=False
    #                     break
    #             if allow:
    #                 u.add(local_s)

    #             del d[:count] 

    #         else:
    #             d.append(str(mantissa[i]))
            
    #     if len(u)==1 and len(mantissa)>1:
    #         for k in u:           
    #             return s[:dot_idx+1]+"("+k+")"
    #     elif len(u)>1:
    #         maxlen=""
    #         for k in u:
    #             if len(k)>len(maxlen):
    #                 maxlen=k
    #         return s[:dot_idx+1]+"("+maxlen+")"
    #     else:
    #         return s
if __name__ == "__main__":
    c=Solution()
    print(c.fractionToDecimal(1,2))#0.5
    print(c.fractionToDecimal(2,1))#2
    print(c.fractionToDecimal(2,3))#0.(6)
    print(c.fractionToDecimal(4,333))#0.(012)
    print(c.fractionToDecimal(1,6))#0.1(6)

            
        
        