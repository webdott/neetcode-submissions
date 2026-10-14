class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        fib = [0 for _ in range(n)]
        fib[0], fib[1] = 1, 2

        for i in range(2, n):
            fib[i] = fib[i - 1] + fib[i - 2]

        return fib[n - 1]