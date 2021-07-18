from collections import defaultdict
class Solution:
    """
    https://leetcode.com/problems/sort-characters-by-frequency/
    """
    def frequencySort(self, s: str) -> str:
        d=defaultdict(int)
        for c in s:
            d[c]+=1
        srt=sorted(d,key=d.get,reverse=True)
        res=[]
        for c in srt:
            res.append(c*d[c])
        return ''.join(res)

if __name__ == "__main__":
    c=Solution()
    print(c.frequencySort('tree'))
        