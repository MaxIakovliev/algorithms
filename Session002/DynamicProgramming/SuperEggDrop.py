class Solution:
    """
    https://leetcode.com/problems/super-egg-drop/description/

    решение взял вот тут:
    https://leetcode.com/problems/super-egg-drop/discuss/159508/easy-to-understand

    """
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        # Я не понимать :'( решения
        memo=[0]*(K+1)
        step=0
        while memo[K]<N:
            for i in range(K,0,-1):
                memo[i]=1+memo[i]+memo[i-1]

            step+=1
        return step