class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        lo = 0
        hi = len(letters)-1
        itarget = ord(target)
        while lo <= hi:
            mid = (int)((lo+hi)/2)
            if ord(letters[mid]) > itarget and mid > 0 and ord(letters[mid-1]) <= itarget:
                return letters[mid]
            elif ord(letters[mid]) > itarget and mid == 0:
                return letters[mid]
            elif ord(letters[mid]) > itarget and mid > 0 and ord(letters[mid-1]) > itarget:
                hi = mid
            elif ord(letters[mid]) > itarget and mid == len(letters)-1:
                return letters[mid]
            elif ord(letters[mid])<=itarget:
                lo=mid+1
        return letters[0]

if __name__ =="__main__":
    c=Solution()
    print(c.nextGreatestLetter( ["c", "f", "j"],"f"))
                
