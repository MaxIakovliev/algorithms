class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(numbers)<2:
            return []
        a =0
        b =len(numbers)-1
        while a!=b:
            cur=numbers[a]+numbers[b]
            if cur==target:
                return [a+1,b+1]
            if cur<target:
                a+=1
            else:
                b-=1
