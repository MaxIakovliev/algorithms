class Solution:
    """
    https://leetcode.com/problems/add-digits/
    
    Solution https://en.wikipedia.org/wiki/Digital_root#Congruence_formula

    """
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1+(num-1)%9
        
        