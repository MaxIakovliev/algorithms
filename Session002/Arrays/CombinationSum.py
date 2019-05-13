class Solution:
    """
    https://leetcode.com/problems/combination-sum/
    """
    def combinationSum(self, candidates: 'List[int]', target: int) -> 'List[List[int]]':
        def solve(data, target, cur, res):
            if target==0:
                if len(cur)==0:
                    return
                tmp=[0]*len(cur)
                for i in range(len(cur)):
                    tmp[i]=cur[i]
                tmp.sort()
                key=str(tmp)
                if key not in self.u:
                    res.append(tmp)
                    self.u.add(key)
                return
            if target<0:
                return
            for i in range(len(data)):
                if data[i]<=target:
                    cur.append(data[i])
                    solve(data,target-data[i],cur,res)
                    cur.pop()
            return
        res=[]
        cur=[]
        self.u=set()
        
        solve(candidates,target,cur,res)
        return res


    def combinationSum2(self, candidates: 'List[int]', target: int) -> 'List[List[int]]':        
        def solve(data, idx, target, cur, res):
            if target==0:
                res.append(cur)
                return
            if target<0:
                return
            for i in range(idx, len(data)):
                solve(data,i,target-data[i],cur+[data[i]],res)
            return
        res=[]
        solve(candidates,0,target,[],res)
        return res
if __name__ == "__main__":
    c=Solution()
    print(c.combinationSum([2,3,6,7],7))        
    print(c.combinationSum([2,3,5],8))        