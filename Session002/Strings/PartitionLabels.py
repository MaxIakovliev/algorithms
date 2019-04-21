class Solution(object):
    """
    https://leetcode.com/problems/partition-labels/
    solution:
    https://leetcode.com/problems/partition-labels/discuss/113259/Java-2-pass-O(n)-time-O(1)-space-extending-end-pointer-solution
    """
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if S is None or len(S)==0:
            return None
        data=[None]*26
        for i in range(len(S)):
            data[ord(S[i])-ord('a')]=i

        last=0
        start=0
        res=[]
        for i in range(len(S)):
            last=max(last,data[ord(S[i])-ord('a')])
            if last==i:
                res.append(last-start+1)
                start=last+1
        return res
if __name__ == "__main__":
    c=Solution()
    print(c.partitionLabels("ababcbacadefegdehijhklij"))



        