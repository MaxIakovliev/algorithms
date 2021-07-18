class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def math(a,b):
            for k,v in b.items():
                if k not in a or a[k]<v:
                    return False
            return True
        if len(s)<len(t):
            return ""
        su={}
        # for c in s:
        #     if c in su:
        #         su[c]+=1
        #     else: 
        #         su[c]=1
        
        tu={}
        for c in t:
            if c in tu:
                tu[c]+=1
            else:
                tu[c]=1
        
       
        start=0
        end=0
        moveStart=True
        moveEnd=True
        res=s
        while end<len(s):
            if s[end] in tu:
                if s[end] not in su:
                    su[s[end]]=1
                else:
                    su[s[end]]+=1
            
            if len(su)==len(tu) and math(su, tu):
                curWord=s[start:end+1]
                if len(res)>len(curWord):
                    res=curWord
                
                while len(su)==len(tu) and start<end:
                    if s[start] in su:
                        su[s[start]]-=1
                        if su[s[start]]<0:
                            su[s[start]]=0
                    else:
                        curWord=s[start+1:end+1]
                        if len(res)>len(curWord):
                            res=curWord


                    start+=1
                    if len(su)!=len(tu) or not math(su,tu):
                        break
            
            end+=1
        while start<end:
            if s[start] in su:
                su[s[start]]-=1
                if su[s[start]]<0:
                    su[s[start]]=0
            else:
                curWord=s[start+1:end+1]
                if len(res)>len(curWord) and curWord!='':
                    res=curWord                    

            start+=1
            if len(su)!=len(tu) or not math(su,tu):
                break

        if s!=t and res==s:
            return ""
        return res

if __name__ =="__main__":
    c=Solution()
    S = "ADOBECODEBANC"
    T = "ABC"
    # print(c.minWindow(S,T))


    S = "AB"
    T = "A"
    # print(c.minWindow(S,T))

    S = "A"
    T = "B"
    # print(c.minWindow(S,T))

    S = "ab"
    T = "A"
    print(c.minWindow(S,T))

        

         