class Solution:
    def toLowerCase(self, s):
        """
        :type str: str
        :rtype: str
        """
        res=[]
        start=ord('a')
        end=ord('z')
        for c in s:
            cur=ord(c)
            if cur >=start and cur <=end:
                res.append(c)
            elif cur>=start-32 and cur<=end-32:
                res.append(chr(cur+32))
            else:
                res.append(c)
        return "".join(res)
if __name__=='__main__':
    c=Solution()
    print(c.toLowerCase("This IS SPARTA"))
