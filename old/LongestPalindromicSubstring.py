class Solution:
    def longestPalindrome(self, s):
        """
        https://leetcode.com/problems/longest-palindromic-substring/description/
        :type s: str
        :rtype: str
        """
        if len(s)<=1:
            return s
        if len(s)==2 and s[0]==s[1]:
            return s
        if len(s)==3 and s[0]==s[2]:
            return s

        start=0
        end=0
        for i in range(0, len(s)):
            for j in range(i, len(s)+1):
                # print("-->"+s[i:j])
                if self.isPalindrome(s,i,j):
                    if j-i>end-start:
                        start=i
                        end=j
                        # res=s[i:j]
        return s[start:end]
                    
    def isPalindrome(self, s, i,j):
        count=1
        k=i
        while k<= j-count:
            if s[k]!=s[j-count]:
                return False
            count+=1
            k+=1
        return True

if __name__=="__main__":
    s=Solution()
    print("brdcecaba->{0}".format(s.longestPalindrome("brdcecaba")))
    print("bab->{0}".format(s.longestPalindrome("bab")))
    print("bb->{0}".format(s.longestPalindrome("bb")))
    print("babad->{0}".format(s.longestPalindrome("babad")))
    print("cbbd->{0}".format(s.longestPalindrome("cbbd")))
    print("a->{0}".format(s.longestPalindrome("a")))