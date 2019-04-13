class Solution:
    """
    https://leetcode.com/problems/backspace-string-compare/
    """
    def backspaceCompare(self, s: str, t: str) -> bool:
        r1=[]
        i=len(s)-1
        removes=0
        while i>=0:
            if s[i]=='#':
                removes+=1
            elif s[i]!='#' and removes>0:
                removes-=1
            else:
                r1.insert(i,s[i])
            i-=1

        removes=0
        r2=[]
        i=len(t)-1
        while i>=0:
            if t[i]=='#':
                removes+=1
            elif t[i]!='#' and removes>0:
                removes-=1
            else:
                r2.insert(i,t[i])
            i-=1
        r1.sort()
        r2.sort()
        # print(f"r1={''.join(r1)}")
        # print(f"r2={''.join(r2)}")

        if (''.join(r1))==(''.join(r2)):
            return True
        return False
if __name__ == "__main__":
    c=Solution()
    c.backspaceCompare("nzp#o#g","b#nzp#o#g")
            