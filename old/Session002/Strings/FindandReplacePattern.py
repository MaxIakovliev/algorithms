class Solution:
    """
    https://leetcode.com/problems/find-and-replace-pattern/
    """
    def findAndReplacePattern(self, words: 'List[str]', pattern: str) -> 'List[str]':
        res=[]
        for word in words:
            if len(word)!= len(pattern):
                continue
            patr={}
            wrd={}
            allow_add=True
            for i in range(len(word)):
                if (word[i] in wrd and pattern[i] not in patr ) \
                or \
                    (word[i] not in wrd and pattern[i] in patr):
                    allow_add=False
                    break
                if word[i] not in wrd and pattern[i] not in patr:
                    wrd[word[i]]=pattern[i]
                    patr[pattern[i]]=word[i]
                elif wrd[word[i]]!=pattern[i]or patr[pattern[i]]!=word[i]:
                    allow_add=False
                    break
            if allow_add:
                res.append(word)
        return res

if __name__ == "__main__":
    c=Solution()
    print(c.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"],'abb'))
    # print(c.findAndReplacePattern(["mee","aqq"],'abb'))
