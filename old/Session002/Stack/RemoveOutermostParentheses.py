class Solution:
    """
    https://leetcode.com/problems/remove-outermost-parentheses/
    """
    def removeOuterParentheses(self, s: str) -> str:
        st=[]
        res=[]
        tmp=[]
        for i in range(len(s)):
            if s[i]=='(':
                st.append('(')
                tmp.append('(')
            else:
                st.pop()
                if len(tmp)>1:
                    tmp.append(')')
                else:
                    tmp.pop()
            if len(st)==0:
                if len(tmp)>2:
                    tmp.pop(0)
                    tmp.pop()
                res.extend(tmp)
                tmp=[]
        

        if len(tmp)>2:
            tmp.pop(0)
            tmp.pop()
        res.extend(tmp)
        tmp=[]
        return ''.join(res)

    def removeOuterParentheses2(self, s: str) -> str:
        stack=0
        res=[]
        tmp=[]
        for i in range(len(s)):
            if s[i]=='(':
                stack+=1
                tmp.append('(')
            else:
                stack-=1
                if len(tmp)>1:
                    tmp.append(')')
                else:
                    tmp.pop()
            if stack==0:
                if len(tmp)>2:
                    tmp.pop(0)
                    tmp.pop()
                res.extend(tmp)
                tmp=[]
        if len(tmp)>2:
            tmp.pop(0)
            tmp.pop()
        res.extend(tmp)
        tmp=[]
        return ''.join(res)


if __name__ == "__main__":
    c=Solution()
    print(c.removeOuterParentheses2("(()())(())"))#()()()
    print(c.removeOuterParentheses2("(()())(())(()(()))"))#()()()()(())
    print(c.removeOuterParentheses2("()()"))#empty

                

                