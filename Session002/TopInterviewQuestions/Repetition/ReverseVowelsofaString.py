class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v=set("aeiouAEIOU")
        lo=0
        hi=len(s)-1
        res=[""]*len(s)
        while lo<=hi:
            if s[lo] in v:
                if s[hi] in v:
                    res[lo]=s[hi]
                    res[hi]=s[lo]
                    lo+=1
                    hi-=1
                else:
                    res[hi]=s[hi]
                    hi-=1
            elif s[hi] in v:
                if s[lo] in v:
                    res[lo]=s[hi]
                    res[hi]=s[lo]
                    lo+=1
                    hi-=1
                else:
                    res[lo]=s[lo]
                    lo+=1
            else:
                res[lo]=s[lo]
                res[hi]=s[hi]
                lo+=1
                hi-=1
        return "".join(res)

