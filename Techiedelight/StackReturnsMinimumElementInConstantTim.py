class StackMin:
    """
    http://www.techiedelight.com/design-stack-which-returns-minimum-element-constant-time/
    
    08/31/2018
    Max
    """
    def __init__(self):
        self.st=list()
        self.aux=list()


    def push(self, val):
        self.st.append(val)
        if len(self.aux)==0:
            self.aux.append(val)
        elif self.aux[-1]>val:
            self.aux.append(val)
    
    def pop(self):
        if self.isEmpty()==True:
            return None
        val=self.st[-1]
        del self.st[-1]
        if len(self.aux)>0 and self.aux[-1]==val:
            del self.aux[-1]
        return val

    def isEmpty(self):
        return len(self.st)==0
    
    def getMin(self):
        if len(self.aux)>0:
            return self.aux[-1]
