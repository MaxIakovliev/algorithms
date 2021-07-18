import collections
class Solution:
    """
    https://leetcode.com/problems/tallest-billboard/
    explanation:
    https://leetcode.com/problems/tallest-billboard/discuss/212047/Python-AC-solution-very-similar-to-Target-Sum-(494)
    """
    def tallestBillboard(self, rods: "List[int]") -> int:
        res={0:0}
        for rod in rods:
            tmp={}
            for k,v in res.items():
                tmp[k+rod]=max(tmp.get(k+rod,0),v+rod)
                tmp[k-rod]=max(tmp.get(k-rod,0),v)
                tmp[k]=max(tmp.get(k,0),v)
            res=tmp
        return res[0]

       

if __name__=="__main__":
    c=Solution()
    c.tallestBillboard([1,2,3])

