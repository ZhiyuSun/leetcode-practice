class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x
        
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


class Solution2:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        else:
            res = self.myPow(x, n//2)
            rest = x if n %2 == 1 else 1
            return res * res * rest


class Solution3:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            ans = 1.0
            x_contribute = x
            while N > 0:
                if N % 2 == 1:
                    ans *= x_contribute
                x_contribute *= x_contribute
                N //= 2
            return ans
        
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)