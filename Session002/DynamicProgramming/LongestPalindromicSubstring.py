class Solution:
    """
    https://leetcode.com/problems/longest-palindromic-substring/description/
    """
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.maxLen=0
        self.lo=0
        def extend(input, j,k):
            while j>=0 and k<len(input) and input[j]==input[k]:
                j-=1
                k+=1
            if self.maxLen<k-j-1:
                self.maxLen=k-j-1
                self.lo=j+1
        ln=len(s)
        if ln<2:
            return s
        for i in range(len(s)-1):
            extend(s,i,i)
            extend(s,i,i+1)
        return s[self.lo:self.lo+self.maxLen]

