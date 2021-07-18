"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        nums = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        tbl=[]
        for i in range(len(digits)):
            tbl.append([digits[i],0])

        result = []
        
        while tbl[0][1]<len(nums[tbl[0][0]]):
            cur = []
            for i in range(len(tbl)):
                x =nums[tbl[i][0]][tbl[i][1]]
                cur.append(x)
                if  i == len(tbl)-1 and tbl[i][1]<len(nums[tbl[i][0]]):
                    tbl[i][1]+=1
                # elif i < len(tbl)-1 and tbl[i+1][1]>=len(nums[tbl[i][0]])-1:
                #     tbl[i][1]+=1

            result.append("".join(cur))
            # print(result)
            # if result[-1]=="afi":
            #     print("here")

            tbl = self.adjust_idxs(tbl, nums)
            if tbl is None:
                break
        return result

    def adjust_idxs(self, tbl, nums):
        idx = len(tbl) - 1
        if tbl[0][1]==len(nums[tbl[0][0]]):
            return None

        processed= False
        while idx>=0:
            if tbl[idx][1]==len(nums[tbl[idx][0]]):
                tbl[idx][1]=0                            
                processed =True
                idx-=1
                while idx>0:
                    if tbl[idx][1]==len(nums[tbl[idx][0]])-1:
                        tbl[idx][1]=0
                        idx-=1
                    else:
                        break

            elif processed:
                tbl[idx][1]+=1
                idx-=1
                break
            else:
                break
            

        if tbl[0][1]>len(nums[tbl[0][0]]):
            return None

        return tbl
            


if __name__ == "__main__":
    c = Solution()
    res = c.letterCombinations("2345")
    print(res)

                
        