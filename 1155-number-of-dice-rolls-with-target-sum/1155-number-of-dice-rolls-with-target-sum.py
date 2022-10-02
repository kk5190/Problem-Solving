class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target > n*k:
            return 0
        div = 10**9 + 7
        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]

        tmin, tmax = max(1, target - (n - 1)*k), min(target - (n - 1), k)
        for t in range(tmin, tmax + 1):
            dp[1][t] = 1

        for m in range(2, n + 1):
            tmin, tmax = max(m, target - (n - m)*k), min(m*k, target - (n - m))
            for t in range(tmin, tmax + 1):
                fmin, fmax = max(1, t - (m - 1)*k), min(t - (m - 1), k)
                for f in range(fmin, fmax + 1):
                    dp[m][t] += dp[m - 1][t - f]
                dp[m][t] = dp[m][t] % div
        
        return dp[n][target]