class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
          return False
        target = total_sum // 2
        n = len(nums)

        dp = [[False for s in range(target + 1)] for i in range(2)]
        dp[0][0] = True

        for i in range(1, n+1):
          for s in range(target + 1):
            if s < nums[i-1]:
              dp[1][s] = dp[0][s]
            else:
              dp[1][s] = dp[0][s] or dp[0][s-nums[i-1]]

          for s in range(target + 1):
            dp[0][s] = dp[1][s]
            dp[1][s] = False
        return dp[0][target]
        