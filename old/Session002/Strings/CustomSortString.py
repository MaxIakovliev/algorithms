class Solution:
    """
    https://leetcode.com/problems/custom-sort-string/
    """
    def customSortString(self, S: str, T: str) -> str:
        decomposition=[[] for _ in range(len(S))]
        rest=[]
        st={}
        for i in range(len(S)):
            st[S[i]]=i
        
        for i in range(len(T)):
            if T[i] in st:
                decomposition[st[T[i]]].append(T[i])
            else:
                rest.append(T[i])
        res=''.join(rest)
        for i in range(len(decomposition)):
            t=''.join(decomposition[i])
            res+=t
        return res
if __name__ == "__main__":
    c=Solution()
    print(c.customSortString("cba","abcd"))



        