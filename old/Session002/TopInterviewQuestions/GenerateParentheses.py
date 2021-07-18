class Solution:
    """
    https://leetcode.com/problems/generate-parentheses/description/
    """
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generateRecursive(cur:str,numOfAvailable:int, numOfUnclosed:int)->(list):
            if numOfAvailable==0:
                return [cur+')'*numOfUnclosed]
            elif numOfUnclosed==0:
                return generateRecursive(cur+'(', numOfAvailable-1, numOfUnclosed+1)

            return generateRecursive(cur+'(',numOfAvailable-1,numOfUnclosed+1)+ generateRecursive(cur+')',numOfAvailable,numOfUnclosed-1)
        
        if n==0:
            return []
        return generateRecursive('',n,0)
if __name__=="__main__":
    c=Solution()
    print(c.generateParenthesis(10))


        