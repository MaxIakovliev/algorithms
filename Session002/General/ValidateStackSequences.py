class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        res=[]
        i=0
        for item in pushed:
            res.append(item)
            while len(res)>0 and res[-1]==popped[i]:
                res.pop()
                i+=1
        return i==len(popped)
if __name__=="__main__":
    c=Solution()
    print(c.validateStackSequences([1,2,3,4,5],[4,5,3,2,1])) #true
    print(c.validateStackSequences([1,2,3,4,5],[4,3,5,1,2])) #false