class Solution:
    """
    https://leetcode.com/problems/powerful-integers/
    """
    def powerfulIntegers(self, x: int, y: int, bound: int):
        res=set()
        i=0
        j=0
        for i  in range(0,100):
            for j in range(0,100):
                t=x**i+y**j
                if t<=bound:
                    res.add(t)
                else:
                    break
        
        return list(res)

if __name__ == "__main__":
    c=Solution()
    print(c.powerfulIntegers(2,3,10))
    print(c.powerfulIntegers(3,5,15))


        