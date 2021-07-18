class Solution:
    """
    https://leetcode.com/problems/reverse-string-ii/description/
    1. reverse k chars if 2k avaiable
    2 reverse all if len<k
    if reverve k chars if len >=k and len <2k

    """
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """