class Solution:
    """
    https://leetcode.com/problems/permutations/submissions/
    solution based on cracking the coding interview p51
    """
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def do_perm(s, pref,res):
            if len(s)==0:
                res.append(pref)
            else:
                for i in range(len(s)):
                    rem=s[:i]+s[i+1:]
                    do_perm(rem,pref+[s[i]],res)
        res=[]
        tmp=[]
        do_perm(nums,tmp, res)
        return res

    def permute2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def do_perm(s, prefix, res):
            if len(s)==0:
                res.append(prefix)
            else:
                for i in range(len(s)):
                    remaining=s[:i]+s[i+1:]
                    do_perm(remaining,prefix+[s[i]], res)
        
        res=[]
        tmp=[]
        do_perm(nums,tmp,res)
        return res

    def permute3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def do_perm(s,prefix,res:list):
            if len(s)==0:
                res.append(prefix)
            else:
                for i in range(len(s)):
                    rest=s[:i]+s[i+1:]
                    do_perm(rest,prefix+[s[i]],res)
        res=[]
        tmp=[]
        do_perm(nums,tmp,res)
        return res


    def permute4(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def do_perm(s, pref, res):
            if len(s)==0:
                res.append(pref)
            else:
                for i in range(len(s)):
                    rest=s[:i]+s[i+1:]
                    do_perm(rest,pref+[s[i]], res)
        tmp=[]
        res=[]
        do_perm(nums,tmp,res)
        return res



    def permute5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def do_perm(s, prefix, res):
            if len(s)==0:
                res.append(prefix)
            else:
                for i in range(len(s)):
                    rest=s[:i]+s[i+1:]
                    do_perm(rest, prefix+[s[i]], res)
        res=[]
        tmp=[]
        do_perm(nums,tmp,res)
        return res
        


    def permute6(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def do_perm(s,prefix,res):
            if len(s)==0:
                res.append(prefix)
            else:
                for i in range(len(s)):
                    rest=s[:i]+s[i+1:]
                    do_perm(rest, prefix+[s[i]],res)
        res=[]
        tmp=[]
        do_perm(nums,tmp,res)
        return res


    def permute7(self, nums):
        def do_perm(s,prefix,res):
            if len(s)==0:
                res.append(prefix)
            else:
                for i in range(len(s)):
                    rest=s[:i]+s[i+1:]
                    do_perm(rest,prefix+[s[i]],res)
        res=[]
        tmp=[]
        do_perm(nums,tmp, res)
        return res



if __name__ == "__main__":
    c=Solution()
    print(c.permute6([1,2,3]))
    
