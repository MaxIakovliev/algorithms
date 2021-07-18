class Solution:
    """
    https://leetcode.com/problems/scramble-string/
    solution:
    https://leetcode.com/problems/scramble-string/discuss/29452/Python-dp-solutions-(with-and-without-memorization).
    """
    def __init__(self):
        self.dic={}

    def isScramble(self, s1: str, s2: str) -> bool:
        if (s1,s2) in self.dic:
            return self.dic[(s1,s2)]
        if len(s1)!=len(s2) or sorted(s1)!=sorted(s2):
            self.dic[(s1,s2)]=False
            return False
        if s1==s2:
            self.dic[(s1,s2)]=True
            return True
        f=self.isScramble
        for i in range(1,len(s1)):
            if (f(s1[i:],s2[i:]) and f(s1[:i], s2[:i])) or\
                (f(s1[i:],s2[:-i]) and f(s1[:i], s2[-i:])):
                return True
        self.dic[(s1,s2)]=False
        return False
if __name__ == "__main__":
    c=Solution()
    print(c.isScramble("great","rgeat"))#true
    print(c.isScramble("abcde","caebd"))#false

        
