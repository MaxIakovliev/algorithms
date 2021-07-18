class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ht={}
        for a in A:
            for b in B:
                if a+b in ht:
                    ht[a+b]+=1
                else:
                    ht[a+b]=1
        count=0
        for c in C:
            for d in D:
                if -c-d in ht:
                    count+=ht[-c-d]
        return count
if __name__ =="__main__":
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]
    c=Solution()
    print(c.fourSumCount(A,B,C,D))