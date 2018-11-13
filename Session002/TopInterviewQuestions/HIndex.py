class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N=len(citations)
        if N==0:
            return 0

        citations=sorted(citations)
        for i in range(N-1,-1,-1):
            if citations[i]<N-i:
                return N-i-1
        return N