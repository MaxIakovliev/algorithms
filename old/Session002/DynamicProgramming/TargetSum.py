from collections import defaultdict

class Solution:
    """
    https://leetcode.com/problems/target-sum/

    solution:
    https://leetcode.com/problems/target-sum/discuss/262783/Python-simple-O(nk)-solution-with-explanation
    """
    def findTargetSumWays(self, nums: 'List[int]', S: int) -> int:
        d= defaultdict(lambda: 0)
        d[nums[0]]+=1
        d[-nums[0]]+=1
        for i in range(1, len(nums)):
            new_d=defaultdict(lambda:0)
            for k, v in d.items():
                new_d[k+nums[i]]+=v
                new_d[k-nums[i]]+=v
            d=new_d
        return d[S]
    
    def findTargetSumWays2(self, nums: 'List[int]', S: int) -> int:
        d = defaultdict(lambda: 0)
        d[nums[0]] += 1
        d[-nums[0]] += 1
        for n in nums[1:]:
            new_d = defaultdict(lambda: 0)
            for k,v in d.items():
                new_d[k+n] += v
                new_d[k-n] += v
            d = new_d
        return d[S]

if __name__ == "__main__":
    c=Solution()
    print(c.findTargetSumWays([0,0,0,0,0,0,0,0,1],1))#256

        