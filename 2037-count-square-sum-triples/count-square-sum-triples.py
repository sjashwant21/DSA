class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for a in range(3, n):
            sqrt_a = a * a
            for b in range(3, n):
                sqrt_sum = sqrt_a + b * b
                c = int(math.sqrt(sqrt_sum))
                if c > n:
                    break
                if c * c == sqrt_sum:
                    cnt += 1
        return cnt 