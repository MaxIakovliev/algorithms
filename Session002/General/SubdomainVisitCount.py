class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        res={}
        for i in range(len(cpdomains)):
            splt=cpdomains[i].split(' ')
            subdomains=splt[1].split('.')
            count=int(splt[0])
            for j in range(0, len(subdomains)):
                cur=".".join(subdomains[j:])
                if cur in res:
                    res[cur]+=count
                else:
                    res[cur]=count
        output=[]
        for k,v in res.items():
            output.append(f"{v} {k}")
        return output
if __name__ == "__main__":
    c=Solution()
    print(c.subdomainVisits(["9001 discuss.leetcode.com"]))
    print(c.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
    
    
        