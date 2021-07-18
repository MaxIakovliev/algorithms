class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a={}
        b={}
        if len(s)!=len(t):
            return False
        for i in range(len(t)):
            if t[i] in a and s[i] in b:
                if a[t[i]]!=s[i] or b[s[i]]!=t[i]:
                    return False
            else:
                if (t[i] in a and s[i] not in b) or (t[i] not in a and s[i] in b):
                    return False
                else:
                    a[t[i]]=s[i]
                    b[s[i]]=t[i]
        return True

            


