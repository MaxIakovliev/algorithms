class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        def swap(input,start,end,data):
            data[end]=input[start]
            data[start]=input[end]
        res=list(s)
        start=0
        end=len(s)-1
        while start<end:
            if s[start].isalpha() and s[end].isalpha():
                swap(s,start,end,res)
                start+=1
                end-=1
            elif not s[start].isalpha():
                res[start]=s[start]
                start+=1
            elif not s[end].isalpha():
                res[end]=s[end]
                end-=1
            else:
                res[start]=s[start]
                start+=1
                res[end]=s[end]
                end-=1
        return ''.join(res)
if __name__ == "__main__":
    c=Solution()
    print(c.reverseOnlyLetters("ab-cd"))
    print(c.reverseOnlyLetters("a-bC-dEf-ghIj"))