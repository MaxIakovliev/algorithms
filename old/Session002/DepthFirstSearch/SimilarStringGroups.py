class Solution:
    """
    https://leetcode.com/problems/similar-string-groups/
    Solution:
    https://leetcode.com/problems/similar-string-groups/discuss/132318/Simple-Java-Solution-using-DFS
    """
    def numSimilarGroups(self, A: "List[str]") -> int:
        def dfs(data,s):
            for item in data:
                if item in self.checked:
                    continue
                if (belong_same_group(item,s)):
                    self.checked.add(item)
                    self.checked.add(s)
                    dfs(data,item)
        def belong_same_group(a,b):
            i=0
            swaps=0
            while swaps<=2 and i<len(a):
                if a[i]!=b[i]:
                    swaps+=1
                i+=1
            return  swaps==2
        if len(A)<2:
            return len(A)
        A=list(set(A))
        self.checked=set()
        res=0
        for i in range(len(A)):
            if A[i] in self.checked:
                continue
            res+=1
            dfs(A,A[i])
        return res

        