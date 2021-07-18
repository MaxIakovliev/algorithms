class Solution:
    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """
        if N==0 or L==0 or N > L:
            return 0
        if N==1 or L==1:
            return 1
        mod=1000000007
        dp=[[0 for j in range(L+1)] for i in range(N+1)]
        dp[0][0]=1
        for l in range(1,L+1):
            for n in range(1,N+1):
                if N-n+1>0:
                    dp[n][l] = ((N - n + 1) * dp[n - 1][l - 1]) % mod
                if n-K>0:
                    dp[n][l] = (dp[n][l] + (((n - K) * dp[n][l - 1]) % mod)) % mod
        return dp[N][L]
