class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minVal=float('inf')
        self.stack=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x<=self.minVal:
            self.stack.append(self.minVal)
            self.minVal=x
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        if self.stack.pop()==self.minVal:
            self.minVal=self.stack.pop()

        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minVal
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()