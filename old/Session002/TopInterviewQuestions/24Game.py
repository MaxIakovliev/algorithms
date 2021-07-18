class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def help_func(arr):
            if len(arr)==1:
                return abs(arr[0]-24.0)<self.eps
            for i in range(len(arr)):
                for j in range(0,i):
                    p1=arr.pop(i)
                    p2=arr.pop(j)
                    nxt=[p1+p2, p2-p1,p1-p2,p2*p1]
                    if abs(p2)>self.eps:
                        nxt.append(float(p1)/float(p2))
    
                    if abs(p1)>self.eps:
                        nxt.append(float(p2)/float(p1))
                    
                    for n in nxt:
                        arr.append(n)
                        if help_func(arr):
                            return True
                        arr.pop()
                    arr.insert(j,p2)
                    arr.insert(i,p1)
            return False


        self.eps = 0.001
        return help_func(nums)
if __name__=="__main__":
    c=Solution()
    print(c.judgePoint24([8,1,6,6]))