class Solution(object):
    """
    https://leetcode.com/problems/plus-one/description/
    """
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i=len(digits)-1
        added=False
        extra=0
        while i>=0:
            if extra==1:
                if digits[i]+extra>9:
                    digits[i]=(digits[i]+1)%10
                    i-=1
                else:
                    digits[i]=digits[i]+1
                    extra=0                
            elif added==False:
                if digits[i]+1>9:
                    digits[i]=(digits[i]+1)%10
                    extra=1
                else:
                    digits[i]+=1
                
                i-=1
                added=True
            else:
                break
        if extra>0:
            digits.insert(0,1)
        return digits
        