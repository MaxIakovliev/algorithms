class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # this is Greedy solution. O(1) space
        pairs=sorted(pairs,key=self.getKey)
        tail=float('-inf')
        res=0
        for i in range(len(pairs)):
            if pairs[i][1]<tail:
                tail=pairs[i][1]
            if pairs[i][0]>tail:
                res+=1
                tail=pairs[i][1]
        return res

 

    
    def getKey(self, a:list)->(int):
        return a[0]

if __name__ == "__main__":
    c = Solution()
    print(c.findLongestChain([[1,2], [2,3], [3,4]]))
    print(c.findLongestChain([[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]))
