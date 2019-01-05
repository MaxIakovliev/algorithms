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
            


if __name__=="__main__":
    c=Solution()
    print(c.letterCasePermutation2("a1b2"))
            
        