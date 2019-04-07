class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        caps=set()
        for c in range(ord('A'), ord('Z')+1):
            caps.add(chr(c))
            count_caps=0
        for i in range(len(word)):
            if word[i] in caps and i>0 and count_caps==0:
                return False
            elif word[i] in caps and i==0:
                count_caps+=1
            elif word[i] in caps and i>0 and count_caps>0:
                count_caps+=1
        if count_caps==0 or count_caps==1 or count_caps==len(word):
            return True
        return False

        