"""
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/perfect-squares
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2020.08.13 在参考了题解，以及错了很多次之后写的
class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i * i for i in range(int(n**0.5)+1, 0, -1)]
        queue = [n]
        res = 0
        while queue:
            res += 1
            queue = list(set(queue))
            for _ in range(len(queue)):
                cur = queue.pop(0)
                for i in square_nums:
                    if cur >= i:
                        next_cur = cur - i
                        if next_cur == 0: return res
                        if next_cur in square_nums:
                            return res + 1
                        queue.append(next_cur)
        return 0
        

# 官方解法。我的解法比官方快一倍
class Solutiongf:
    def numSquares(self, n):

        # list of square numbers that are less than `n`
        square_nums = [i * i for i in range(1, int(n**0.5)+1)]
    
        level = 0
        queue = {n}
        while queue:
            level += 1
            #! Important: use set() instead of list() to eliminate the redundancy,
            # which would even provide a 5-times speedup, 200ms vs. 1000ms.
            next_queue = set()
            # construct the queue for the next level
            for remainder in queue:
                for square_num in square_nums:    
                    if remainder == square_num:
                        return level  # find the node!
                    elif remainder < square_num:
                        break
                    else:
                        next_queue.add(remainder - square_num)
            queue = next_queue
        return level
