MOD = 10**9 + 7

class Solution(object):
    def numberOfWays(self, n, x):
        # build list of i**x <= n
        vals = []
        i = 1
        while True:
            p = i ** x
            if p > n:
                break
            vals.append(p)
            i += 1

        # dp[s] = number of ways to make sum s using each value at most once
        dp = [0] * (n + 1)
        dp[0] = 1

        for v in vals:
            # iterate backwards to ensure each v is used at most once
            for s in range(n, v - 1, -1):
                dp[s] = (dp[s] + dp[s - v]) % MOD

        return dp[n]