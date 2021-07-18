class Solution:
    def repeatedNTimes(self, A: "List[int]") -> int:
        u=set()
        for i in A:
            if i in u:
                return i
            else:
                u.add(i)
        return -1