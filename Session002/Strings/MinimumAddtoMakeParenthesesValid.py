class Solution:
    """
    https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
    """
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        res=0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(s[i])
            else:
                if len(stack)==0:
                    res+=1
                else:
                    stack.pop()
        res+=len(stack)
        return res
if __name__ == "__main__":
    c=Solution()
    print(c.minAddToMakeValid('())'))#1
    print(c.minAddToMakeValid('()'))#0
    print(c.minAddToMakeValid('((('))#3
    print(c.minAddToMakeValid(')))'))#3
    print(c.minAddToMakeValid(')()))'))#3
    print(c.minAddToMakeValid('()))(('))#4


        