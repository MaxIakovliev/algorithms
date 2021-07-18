class Solution:
    """
    https://leetcode.com/problems/delete-columns-to-make-sorted-ii/
    """
    def minDeletionSize(self, A: 'list[str]') -> int:
        idx=set()
        i=1
        while i<len(A):
            for j in range(len(A[i])):
                if j in idx or A[i-1][j]==A[i][j]:
                    continue
                if A[i-1][j]>A[i][j]:
                    idx.add(j)
                    i=0
                break
            i+=1
        return len(idx)

if __name__=="__main__":
    c=Solution()
    print(c.minDeletionSize(["zyx","wvu","tsr"])) #3
    print(c.minDeletionSize(["ca","bb","ac"]))#1
    print(c.minDeletionSize(["xc","yb","za"]))#0
    print(c.minDeletionSize(["jwkwdc","etukoz"]))#2
    

        