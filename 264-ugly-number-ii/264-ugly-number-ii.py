class Solution:
    def nthUglyNumber(self, n: int) -> int:
        allowed_primes = (2, 3, 5)
        ans = [1]
        used = {1}
        for _ in range(n-1):
            val = heappop(ans)
            for prime in allowed_primes:
                if val * prime not in used:
                    heappush(ans, val * prime)
                    used.add(val * prime)
        return ans[0]
        