class Solution:
    def productQueries(self, n, queries):
        MOD = 10**9 + 7

        # Build powers[]: the powers of two corresponding to set bits of n,
        # in non-decreasing order
        powers = []
        bit = 1
        x = n
        while x:
            if x & 1:
                powers.append(bit)
            bit <<= 1
            x >>= 1

        # prefix products modulo MOD
        m = len(powers)
        prefix = [0] * m
        prefix[0] = powers[0] % MOD
        for i in range(1, m):
            prefix[i] = (prefix[i-1] * powers[i]) % MOD

        # Precompute modular inverses of prefix products
        inv_prefix = [0] * m
        for i in range(m):
            inv_prefix[i] = pow(prefix[i], MOD - 2, MOD)

        # Answer queries
        ans = []
        for L, R in queries:
            if L == 0:
                ans.append(prefix[R])
            else:
                ans.append((prefix[R] * inv_prefix[L-1]) % MOD)

        return ans