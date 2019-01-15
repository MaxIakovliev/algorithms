import bisect
class Solution:
    """
    https://leetcode.com/problems/odd-even-jump/description/

    good solution:
    https://leetcode.com/problems/odd-even-jump/discuss/218264/Python-Map-value-to-index
    """
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n=len(A)
        odd=[False]*n
        even=[False]*n

        odd[-1]=True
        even[-1]=True
        
        valueToIdx={A[n-1]:n-1}
        vals=[A[n-1]]
        numVals=1
        for i in range(n-2,-1,-1):
            v=A[i]
            if v in valueToIdx:
                odd[i]=even[valueToIdx[v]]
                even[i]=odd[valueToIdx[v]]
            else:
                idx=bisect.bisect(vals,v)

                if idx!=0:
                    lower=vals[idx-1]
                    even[i]=odd[valueToIdx[lower]]
                if idx!=numVals:
                    higher=vals[idx]
                    odd[i]=even[valueToIdx[higher]]
                vals.insert(idx, v)
                numVals+=1
            valueToIdx[v]=i
        return sum(odd)