class Solution:
    def fib(self, N: int) -> int:
        # 0, 1, 1, 2, 3, 5, 8, 13...
        if N <= 1:
            return N

        #数值交换
        a, b = 0, 1
        # for n in range(N-1):
        #     a, b = b, a+b
        # return b
        while N > 1:
            a, b = b, a+b
            N -= 1
        return b

    # 递归方式
    def fib1(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib1(n - 1) + self.fib1(n - 2)

r = Solution().fib(6)
print(r)
