class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a={}
        b={}
        for c in s:
            if c in a:
                a[c]+=1
            else:
                a[c]=1

        for c in t:
            if c in b:
                b[c]+=1
            else:
                b[c]=1

        if len(a)!=len(b):
            return False
        
        for key,val in a.items():
            found=False
            for key1, val1 in b.items():
                if val==val1:
                    del a[key]
                    del b[key1]
                    found=True
                    break
            if found==False:
                return False
        if len(a)>0 or len(b)>0:
            return False
        return True
            
