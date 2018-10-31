class Solution:
    """
    https://leetcode.com/problems/keyboard-row/description/
    """
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        arr=[]
        res=[]
        arr.append(set(list('qwertyuiop')))
        arr.append(set(list('asdfghjkl')))
        arr.append(set(list('zxcvbnm')))
        for word in words:
            for i in range(len(arr)):
                add=True
                for c in word.lower():
                    if c not in arr[i]:
                        add=False
                        break
                if add:
                    res.append(word)

        return res
if __name__=="__main__":
    c=Solution()
    print(c.findWords(["Hello", "Alaska", "Dad", "Peace"]))
            
        