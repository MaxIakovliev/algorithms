class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        lo=0
        hi=len(letters)
        target_int=ord(target)
        res=ord(letters[len(letters)-1])
        if target_int>=res:
            return letters[0]
        while lo<hi:
            mid=(int)((lo+hi)/2)
            cur_int=ord(letters[mid])
            if cur_int<=target_int:
                lo=mid+1
            elif cur_int>target_int:
                res=min(res, cur_int)
                hi=mid
            
        return chr(res)

if __name__=="__main__":
    c=Solution()
    print(c.nextGreatestLetter(["c", "f", "j"],"a")) #c
    print(c.nextGreatestLetter(["c", "f", "j"],"c")) #f
    print(c.nextGreatestLetter(["c", "f", "j"],"d")) #f
    print(c.nextGreatestLetter(["c", "f", "j"],"g")) #j
    print(c.nextGreatestLetter(["c", "f", "j"],"k")) #c
    print(c.nextGreatestLetter(["c", "f", "j"],"j")) #c
            
                    