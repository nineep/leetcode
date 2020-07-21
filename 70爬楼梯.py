import functools
class Solution:

    # 递归
    @functools.lru_cache(100)  # 缓存装饰器
    def climbStairs(self, n:int)-> int:
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    # 动态规划空间复杂度O(n)
    def climbStairs2(self, n):
        dp = {}
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    # 动态规划空间复杂度O(1)
    def climbStairs3(self, n):
        if n ==1 or n==2:
            return n
        a, b, temp = 1, 2, 0
        for i in range(3, n+1):
        #     temp = a+b
        #     a, b = b, temp
        # return temp
            a, b = b, a+b
        return b

a = Solution().climbStairs3(5)
print(a)