class LongestSubstringWithoutRepeating:
    """
    https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
    """
    def lengthOfLongestSubstring(self, s):
        di={}
        count=0
        start=0
        res=0
        for ch in s:
           
            if ch not in di:
                di[ch]=count
            else:
                start=max(di[ch]+1,start)
                di[ch]=count
            count+=1
            res=max(res, count-start)
        return res            
 
                

if __name__ =='__main__':
    c=LongestSubstringWithoutRepeating()
    print("expected 0 - actual "+str( c.lengthOfLongestSubstring("")))
    print("expected 1 - actual "+str( c.lengthOfLongestSubstring("a")))
    print("expected 2 - actual "+str( c.lengthOfLongestSubstring("ab")))
    print("expected 2 - actual "+str( c.lengthOfLongestSubstring("abb")))
    print("expected 3 - actual "+str( c.lengthOfLongestSubstring("abcaaa")))
    print("expected 1 - actual "+str( c.lengthOfLongestSubstring("aa")))
    print("expected 1 - actual "+str( c.lengthOfLongestSubstring("aaa")))
    print("expected 2 - actual "+str( c.lengthOfLongestSubstring("aaabaaa")))
    print("expected 3 - actual "+str( c.lengthOfLongestSubstring("aaabcaaa")))
    print("expected 4 - actual "+str( c.lengthOfLongestSubstring("aaabcaaabcdaa")))
    print("expected 3 - actual "+str( c.lengthOfLongestSubstring("pwwkew")))
#abaaa