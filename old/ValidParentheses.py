class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=list()
        for  c in s:
            if c=='(' or c=='[' or c=='{':
                st.append(c)
            elif c==')':
                if len(st)==0:
                    return False
                m=st.pop()
                if m!='(':
                    return False
            elif c==']':
                if len(st)==0:
                    return False
                m=st.pop()
                if m!='[':
                    return False
            elif c=='}':
                if len(st)==0:
                    return False
                m=st.pop()
                if m!='{':
                    return False
            
        if len(st)>0:
            return False
        
        return True
if __name__=='__main__':
    c=Solution()
    print(str(c.isValid('()')))
    print(c.isValid('((()))'))
    print(c.isValid('()[]{}(([]))'))
    print(c.isValid('(()))'))
    