class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for c in s:
            if c=='(' or c=="[" or c=="{":
                stack.append(c)
            else:
                if len(stack)==0:
                    return False
                a=stack.pop()
                if ( c==')' and a!='(') or (c==']' and a!='[') or (c=='}' and a!='{'):
                    return False

        if len(stack)==0:
            return True
        return False

if __name__ =="__main__":
    c=Solution()
    print(c.isValid('{}'))
    print(c.isValid('[]'))
    print(c.isValid('()'))
    print(c.isValid('('))
    print(c.isValid('(}'))
    print(c.isValid('[]}'))
