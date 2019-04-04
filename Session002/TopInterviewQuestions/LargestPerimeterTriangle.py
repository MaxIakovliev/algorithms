class Solution:
    """
    https://leetcode.com/problems/largest-perimeter-triangle/
    """
    def largestPerimeter(self, arr: "List[int]") -> int:
        def calc(a,b,c):
            if a+b<=c or a+c<=b or b+c<=a:
                return -1
            return a+b+c

        if len(arr)<3:
            return 0
        arr.sort()
        i=len(arr)-1
        a=0
        b=0
        c=0
        
        while i>=1:
            a=arr[i]
            b=arr[i-1]
            c=arr[i-2]
            res=calc(a,b,c)
            if res>0:
                return res
            i-=1
        return 0
if __name__ == "__main__":
    c=Solution()
    print(c.largestPerimeter([2,1,2]))#5
    print(c.largestPerimeter( [1,2,1]))#0
    print(c.largestPerimeter(  [3,2,3,4]))#10
    print(c.largestPerimeter(  [3,6,2,3]))#8



        