class Solution:
    """
    https://leetcode.com/problems/letter-case-permutation/description/
    """
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        BFS solution
        """
        if len(S)==0:
            return [""]
        queue=[]
        queue.append(S)

        for i in range(len(S)):
            if ord(S[i])>=ord('0') and ord(S[i])<=ord('9'):
                continue
            for j in range(len(queue)):
                cur=queue.pop(0)
                newStr=cur[:i]+cur[i].upper()+cur[i+1:]
                queue.append(newStr)

                newStr=cur[:i]+cur[i].lower()+cur[i+1:]
                queue.append(newStr)
        return queue

    def letterCasePermutation2(self, S):
        """
        :type S: str
        :rtype: List[str]
        DFS solution
        """
        def dfs(arr,word, pos):
            if pos==len(word):
                arr.append(word)
                return
            if ord(word[pos])>=ord('0') and ord(word[pos])<=ord('9'):
                dfs(arr,word,pos+1)
                return
            newWord=word[:pos]+word[pos].lower()+word[pos+1:]
            dfs(arr,newWord,pos+1)

            newWord=word[:pos]+word[pos].upper()+word[pos+1:]
            dfs(arr,newWord,pos+1)
        res=[]
        dfs(res,S,0)
        return res
            


    def letterCasePermutation3(self, S):
        """
        :type S: str
        :rtype: List[str]
        DFS solution
        """
        def dfs(word, pos,res):
            if pos==len(word):
                res.append(word)
                return
            if ord(word[pos])>=ord('0') and ord(word[pos])<=ord('9'):
                dfs(word,pos+1,res)
            else:
                newWord=word[:pos]+word[pos].lower()+word[pos+1:]
                dfs(newWord,pos+1,res)

                newWord=word[:pos]+newWord[pos].upper()+word[pos+1:]
                dfs(newWord,pos+1,res)
        res=[]
        dfs(S,0,res)
        return res



    def letterCasePermutation4(self, S):
        """
        :type S: str
        :rtype: List[str]
        DFS solution
        """
        def dfs(word, pos, res):
            if pos==len(word):
                res.append(word)
                return
            elif ord(word[pos])>= ord('0') and ord(word[pos])<=ord('9'):
                dfs(word,pos+1,res)
            else:
                new_word=word[:pos]+word[pos].lower()+word[pos+1:]
                dfs(new_word,pos+1,res)
                new_word=word[:pos]+word[pos].upper()+word[pos+1:]
                dfs(new_word,pos+1,res)
            return
        res=[]
        dfs(S,0,res)
        return res

    

if __name__=="__main__":
    c=Solution()
    print(c.letterCasePermutation4("a1b2"))
            
        