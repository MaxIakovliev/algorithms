class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        data={}
        for c in s:
            if c not in data:
                data[c]=1
            else:
                data[c]+=1
        for c in t:
            if c not in data:
                return False
            else:
                data[c]-=1
            if data[c]==0:
                del data[c]
        if len(data)>0:
            return False
        return True

if __name__ =="__main__":
    c=Solution()
    print(c.isAnagram("anagram","nagaram"))
    print(c.isAnagram("rat","cat"))