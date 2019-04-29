class Solution:
    """
    https://leetcode.com/problems/camelcase-matching/
    """
    def camelMatch(self, q: 'List[str]', pattern: str) -> 'List[bool]':
        res=[False]*len(q)
        for i in range(len(q)):
            t=[]
            idx=0
            for j in range(len(q[i])):
                if idx>=len(pattern) and ord(q[i][j])>=ord('A') and ord(q[i][j])<=ord('Z'):
                    idx+=1
                    break

                if ord(q[i][j])>=ord('A') and ord(q[i][j])<=ord('Z') and ord(pattern[idx])>=ord('A') and ord(pattern[idx])<=ord('Z') and pattern[idx]!=q[i][j]:
                    idx=len(pattern)+1
                    break

                if  idx<len(pattern) and pattern[idx]==q[i][j]:
                    idx+=1
            if idx==len(pattern):
                res[i]=True

        return res
if __name__ == "__main__":
    c=Solution()
    print(c.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"],"FB")) #[true,false,true,true,false]
    print(c.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"],"FoBa")) #[true,false,true,false,false]