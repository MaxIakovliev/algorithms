class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def validate(st):
            if st in self.wrong:
                return
            stack=[]
            res=[]
            i=0
            for s in st:
                if s=='(':
                    stack.append(s)
                    res.append(s)
                elif s==')':
                    if len(stack)==0:
                        break
                    else:
                        stack.pop()
                    res.append(s)
                else:
                    res.append(s)
                i+=1
            if i==len(st) and len(stack)==0:
                if  len(res)>0:
                    tmp="".join(res)
                    if tmp not in self.u:
                        if len(tmp)<self.maxSoFar:
                            return
                        else:
                            self.result.append(tmp)
                            self.u.add(tmp)
                            self.maxSoFar=len(tmp)
                return
            else:
                self.wrong.add(st)
                for i in range(len(st)):
                    if st[i]==')' or st[i]=='(':
                        validate(st[:i]+st[i+1:])
    

        self.wrong=set()
        self.maxSoFar=0
        self.result=[]
        self.u=set()
        validate(s)
        i=0
        while i<len(self.result):
            if len(self.result[i])<self.maxSoFar:
                del self.result[i]
            else:
                i+=1
        if len(self.result)==0:
            self.result.append("")
        return self.result
if __name__=="__main__":
    c=Solution()
    print(c.removeInvalidParentheses("()())()"))
    print(c.removeInvalidParentheses("(a)())()"))
    print(c.removeInvalidParentheses(")("))
    print(c.removeInvalidParentheses(")()()(((t"))
    print(c.removeInvalidParentheses(")(((((((("))
    print(c.removeInvalidParentheses("(((()(((()"))
    print(c.removeInvalidParentheses("()((())h()(()()()))(("))


                

